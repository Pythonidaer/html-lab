# HTML Lab

An independent HTML reference and playground, designed around complete example contexts.

## Catalog

- 113 standard HTML element types, with headings counted individually.
- 144 unique regular attribute names and 89 event handler names: 233 indexed attributes.
- Nine practical element categories; attribute filters distinguish global, element-specific, shadow DOM, and event handlers.
- Source snapshot: WHATWG HTML index, October 4, 2026.
- Obsolete features, ARIA, SVG/MathML catalogs, and attributes from other specifications are excluded. Custom data attributes are represented as a family in element controls.

## Explore

Search either catalog. Choose an element or attribute, adjust its settings, and compare the complete live example. Each target includes required parents, children, and related controls. The context note explains those relationships; the document inspection panel reports attributes and hidden/nonvisual features.

Examples cover tables, form labels and validation, image maps, disclosure controls, modal dialogs, local playable media, templates, scripts, shadow DOM slots, and document metadata. Attribute examples select a relevant element and add special supporting controls for popovers, commands, external form associations, and declarative shadow DOM. Users can choose among elements that accept an attribute.

The HTML editor supports complete documents and fragments. Keep `data-lab-target` on the element to control; template content is also searched. Scripts execute only in a sandboxed frame without same-origin access. Navigation and form submissions are intercepted. Changes reset on refresh; there is no database.

## Limits

Interface recognition is only a partial browser-support hint, not a compatibility certification. Setting an attribute does not prove the browser implements its behavior. Inspect the original standard for conditional rules.

Server submission, real downloads, popups, metadata indexing, and every lifecycle event cannot be fully exercised in the isolated preview. Relevant examples disclose these limits. Event handlers provide a starting context and log observed events; some events need conditions beyond that example. Newer features may be experimental or unsupported.

No finite catalog lists all author-defined strings, URLs, numeric values, JavaScript programs, or custom data names. Value grammar is included, with editable values and representative presets.

## Files and preview

`dist/` is the complete buildless static website. Run `python3 -m http.server 8000 --directory dist` and open http://localhost:8000.

The published site is https://pythonidaer.github.io/html-lab/. Pushes to `main` deploy `dist/` with GitHub Pages.

`dist/catalog.json` is the source snapshot; `dist/data.js` is its browser wrapper. `build-catalog.py` documents extraction of the WHATWG tables. It fetches the live index; review counts and regenerate data.js when updating. The script requires Python's standard library. Sample video/audio and captions are local fixtures.

## Validation

JavaScript syntax checks, unique catalog counts, one complete target example per element, and fixture/reference checks. Browser rendering and interoperability still need a manual review in your browser.

## Future improvements

- Explain what every element, attribute, and value is doing in plain language, so a reader can understand the effect without first reading the standard.
- Review the interface components for usability: search, filters, controls, the live preview, the editor, and the reference panels.
- Check that each example is a sensible demonstration of its target, with context that matches how the element or attribute is actually used.

## Sources

https://html.spec.whatwg.org/multipage/indices.html

Descriptions, content models, and attribute grammars derive from the WHATWG HTML standard; original examples, context explanations, and interface code accompany them. Per-entry links open the source. HTML Lab does not represent an official WHATWG project.
