# Adam Riddick — personal site

Personal CV and architecture portfolio for Adam Riddick, built with Astro, TypeScript and Tailwind CSS.

Source repository: [AdamRiddick/riddick.dev](https://github.com/AdamRiddick/riddick.dev). Hosting is not yet configured.

## Brand and writing direction

The established theme applies to all public-facing artifacts. See [the brand guide](docs/brand.md) and [the researched editorial proposal](docs/editorial-strategy.md). Writing preferences are recorded; the proposed article format and topics are not yet implemented. The reusable [Adam Riddick writing skill](skills/adam-riddick-writing/SKILL.md) includes a [versioned voice profile](skills/adam-riddick-writing/references/voice.md), an article workflow and a brief template. The voice will be refined through Adam's edits.

## Run locally

Requires Node.js >=22.23.4, as declared by the locked Astro release. This first pass was verified with Node 26.10.0.

```sh
npm ci
npm run dev
```

## Check and build

```sh
npm run check
npm run build
npm run check:output
```

The static site is generated into `dist/`. There is no server adapter, database, analytics or remote font dependency. The only browser JavaScript closes the mobile menu after selecting a link. Email links open the visitor's email application.

## Edit the content

- `src/pages/index.astro`: homepage copy, expertise and career history.
- `src/content/work/*.md`: the three case studies. Frontmatter is checked by the content schema.
- `src/components/Architecture.astro`: original conceptual illustration, not a representation of a private production topology.
- `src/styles/global.css`: Tailwind theme and custom editorial styling.
- `src/layouts/Layout.astro`: shared navigation, metadata and footer.
- `public/adam-riddick-cv.pdf`: masked public CV styled to match the website.
- `scripts/cv-content.json`: public CV content, separate from PDF layout.
- `scripts/fonts/`: embedded website typefaces for PDF generation, with their SIL Open Font Licenses.

To regenerate the public CV, install Python's `reportlab` package and run `python3 scripts/build-public-cv.py`. Python is not required for Cloudflare's site build. The generator embeds the committed DM Sans, Instrument Serif and IBM Plex Mono fonts, uses the website palette and keeps the document to two A4 pages. Review both rendered pages after regenerating, and verify text extraction, masking and contact links before publishing.

## Content provenance and masking

Career facts and outcomes come from Adam's supplied CV, reviewed on 3 November 2026. The four Top Talent Awards, Platinum recognition, ownership emphasis and preferred contact address were supplied directly by Adam on 4 November 2026. Reference sites informed presentation only; their personal achievements, employers and specialist claims were not transferred.

Approved public figures: 13+ years' experience, 2 million+ monthly users of the live reporting/integration/authentication services, and £25m+ ARR of the portfolio Adam helped lead. Revenue is portfolio context, not revenue personally generated. Other commercial performance figures and exact team sizes are generalised in both site content and the downloadable PDF. Role dates, identity protocol names, award years and technical qualifications are retained. The original private CV is not included.

The cloud and recovery case study explicitly combines separate initiatives across the architecture and engineering leadership roles. Case studies describe team delivery with Adam's architectural or management responsibility, not sole implementation.

Before a public launch, review the wording, confirm engagement preferences and availability, and add the final domain for canonical URLs, sitemap and social sharing imagery. A portrait can be added when a suitable photo is supplied; the current identity artwork does not depict a person.

The 4 November revision tightens page spacing, expands the conceptual architecture illustration and presents the case studies around shared delivery, Adam's contribution and continuity of team ownership. FinOps describes the cost optimisation work already documented in the CV. The site and public CV now use `adam@riddick.dev`; mailbox setup is managed separately.

## Cloudflare Pages (when ready)

Connect this GitHub repository to Cloudflare Pages:

- Production branch: `main`
- Build command: `npm run build`
- Output directory: `dist`
- Pin a Cloudflare-supported Node version compatible with the committed Astro release.

Use Cloudflare's Git integration for preview deployments. No Cloudflare adapter is needed for this static build. `public/_headers` contains basic response headers. Domain-specific SEO and deployment configuration should be completed once the public domain is confirmed.
