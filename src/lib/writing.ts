export function visibleArticles<T extends { data: { draft: boolean } }>(
  articles: T[],
  includeDrafts = false,
): T[] {
  return articles.filter((article) => includeDrafts || !article.data.draft);
}

export function formatPublicationMonth(month: string): string {
  if (!/^\d{4}-(0[1-9]|1[0-2])$/.test(month))
    throw new Error("Publication month must use YYYY-MM.");
  const [year, value] = month.split("-").map(Number);
  return new Intl.DateTimeFormat("en-GB", {
    month: "long",
    year: "numeric",
    timeZone: "UTC",
  }).format(new Date(Date.UTC(year, value - 1, 1)));
}

export function articleLabel(data: {
  draft: boolean;
  publicationMonth?: string;
}): string | undefined {
  if (data.draft) return undefined;
  if (!data.publicationMonth)
    throw new Error("Published articles require a publication month.");
  return formatPublicationMonth(data.publicationMonth);
}

export function readingMinutes(body: string): number {
  return Math.max(1, Math.ceil(body.trim().split(/\s+/).length / 220));
}
