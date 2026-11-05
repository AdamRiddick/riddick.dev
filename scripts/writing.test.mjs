import test from "node:test";
import assert from "node:assert/strict";
import {
  visibleArticles,
  articleLabel,
  formatPublicationMonth,
} from "../src/lib/writing.ts";

test("unpublished drafts are excluded unless preview is explicitly enabled", () => {
  const published = {
    id: "published",
    data: { draft: false, publicationMonth: "2026-11" },
  };
  const draft = { id: "draft", data: { draft: true } };
  assert.deepEqual(visibleArticles([draft, published]), [published]);
  assert.deepEqual(visibleArticles([draft, published], false), [published]);
  assert.deepEqual(visibleArticles([draft, published], true), [
    draft,
    published,
  ]);
});
test("a draft never acquires an implied publication date", () => {
  assert.equal(articleLabel({ draft: true }), "Draft");
  assert.equal(
    articleLabel({ draft: true, publicationMonth: "2023-04" }),
    "Draft",
  );
  assert.throws(
    () => articleLabel({ draft: false }),
    /require a publication month/,
  );
});
test("publication labels preserve month precision and reject invalid dates", () => {
  assert.equal(formatPublicationMonth("2026-11"), "November 2026");
  assert.equal(formatPublicationMonth("2024-01"), "January 2024");
  for (const invalid of [
    "2026-00",
    "2026-13",
    "2026-11-05",
    "2026-1",
    "not-a-date",
  ])
    assert.throws(() => formatPublicationMonth(invalid));
});
