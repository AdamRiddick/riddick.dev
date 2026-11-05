# Working on riddick.dev

Read [README.md](README.md) and [docs/brand.md](docs/brand.md) before changes to the site or related public-facing artifacts. The brand applies across the website, public CV, articles, diagrams and downloadable resources.

Preserve the approved facts, masking and team-centred voice. Do not invent professional experience, outcomes or historical publication dates. Follow the confirmed writing preferences in the brand guide; distinguish them from the proposed format and topics in [docs/editorial-strategy.md](docs/editorial-strategy.md).

When drafting or revising Adam's articles, read [the writing skill](skills/adam-riddick-writing/SKILL.md) and follow its linked voice profile. Learn from Adam's edits; do not treat unedited agent prose as an established voice sample. The first profile is intentionally provisional because no representative long-form samples are available yet.

For site changes, run `npm run check`, `npm run build` and `npm run check:output`. For PDF changes, regenerate using `scripts/build-public-cv.py`, visually review both rendered pages, and check text extraction and masking. The public CV's content is in `scripts/cv-content.json`.

Keep dependencies, generated output, local environment files and private source documents out of Git. Future work should use a scoped branch and inspect the working tree before editing. Do not introduce comments, a CMS, analytics, subscription collection or server-side features merely to support the writing section.
