import { readdir, readFile, stat } from "node:fs/promises";
import { resolve, dirname, extname } from "node:path";
const root = resolve("dist");
const walk = async (dir) =>
  (
    await Promise.all(
      (await readdir(dir, { withFileTypes: true })).map((e) =>
        e.isDirectory() ? walk(resolve(dir, e.name)) : resolve(dir, e.name),
      ),
    )
  ).flat();
const files = await walk(root);
const html = files.filter((f) => extname(f) === ".html");
const failures = [];
for (const file of html) {
  const body = await readFile(file, "utf8");
  if (!/<html[^>]*lang="en-GB"/.test(body))
    failures.push(`${file}: missing document language`);
  if ((body.match(/<h1[\s>]/g) || []).length !== 1)
    failures.push(`${file}: expected one main heading`);
  if (
    /£\s?330|\b330k\b|\b25%|\b40\+|eight teams|eight hours|two hours|tripling|tripled|75%|90%/i.test(
      body,
    )
  )
    failures.push(`${file}: a masked figure appeared`);
  if (body.includes("adam.riddick@icloud.com"))
    failures.push(`${file}: outdated email address`);
  if (/mailto:/.test(body) && !body.includes("mailto:adam@riddick.dev"))
    failures.push(`${file}: missing preferred email address`);
  for (const [, href] of body.matchAll(/href="([^"]+)"/g)) {
    if (/^(https?:|mailto:|tel:|data:)/.test(href)) continue;
    const [path, fragment] = href.split("#");
    let dest = path
      ? resolve(
          path.startsWith("/") ? root : dirname(file),
          path.replace(/^\//, ""),
        )
      : file;
    try {
      if ((await stat(dest)).isDirectory()) dest = resolve(dest, "index.html");
      await stat(dest);
    } catch {
      failures.push(`${file}: broken link ${href}`);
      continue;
    }
    if (fragment && extname(dest) === ".html") {
      const target = await readFile(dest, "utf8");
      if (!target.includes(`id="${decodeURIComponent(fragment)}"`))
        failures.push(`${file}: missing anchor ${href}`);
    }
  }
}
const homepage = await readFile(resolve(root, "index.html"), "utf8");
for (const text of [
  "FinOps",
  "Made in the United Kingdom",
  "Top Talent Awards",
  "Platinum recognition",
  "Annual recurring revenue across the portfolio",
]) {
  if (!homepage.includes(text))
    failures.push(`Homepage: missing requested content ${text}`);
}
for (const file of html.filter((f) => f.includes("/work/"))) {
  const body = await readFile(file, "utf8");
  if (
    !body.includes("MY PART IN THE TEAM") ||
    !body.includes("What carried forward")
  )
    failures.push(`${file}: missing team contribution or continuity content`);
}
if (!files.some((f) => f.endsWith("/adam-riddick-cv.pdf")))
  failures.push("Public CV is missing");
if (failures.length) {
  console.error(failures.join("\n"));
  process.exit(1);
}
console.log(
  `Passed: ${html.length} HTML pages, internal links, anchors, public CV presence and masked-figure checks.`,
);
