let initialDataCache;

export function readInitialData() {
  if (initialDataCache !== undefined) {
    return initialDataCache;
  }
  const element = document.getElementById("docupilotInitialData");
  if (!element) {
    initialDataCache = {};
    return initialDataCache;
  }
  try {
    initialDataCache = JSON.parse(element.textContent || "{}") || {};
  } catch {
    initialDataCache = {};
  }
  return initialDataCache;
}
