# README - style

We define the styles for HTML construction per a base stylesheet derived from
the OASIS initial provisioned stylesheet (cf. below "Changes") and name the
file containing these base CSS style definitions `base.css`.

We add the style layer that provides most of the look of published OASIS workproducts
per the local stylesheet `skin.css`.

## Changes

We started from <https://docs.oasis-open.org/templates/css/markdown-styles-v1.7.3a.css>
and then added custom styles to maintain a clean normative source in markdown and stiil
produce an easy to navigate and read HTML format document.

Later we added the `markdown-styles-v1.7.3b.css` stylesheet, a customization from Heiko Theißen
of the OData TC that adds local fonts to the OASIS provisioned stylesheet and is available at
<https://raw.githubusercontent.com/oasis-tcs/odata-specs/main/docs/odata-data-aggregation-ext/styles/markdown-styles-v1.7.3b.css>.
The change is documented at <https://github.com/oasis-tcs/odata-specs/commit/de2fef7d27c863e63c8ff2eec86b0432c066a628>
while the real changes are per:
<https://github.com/oasis-tcs/odata-specs/commit/696b77719#diff-85cd50d314b2e6e55fe45d6f3daa6cf47a2ebab7a33b5ef33efa0b7601c51fb7>
within the old file (name with the `a`).

As a service:

```diff
--- markdown-styles-v1.7.3a.css	2023-12-09 13:11:55
+++ markdown-styles-v1.7.3b.css	2023-12-09 13:30:03
@@ -12,11 +12,12 @@
 /* pk 2019-05-23 - v1.7.2 (based on 1.7.1) changed monospace "code" font to Courier New */
 /* pk 2019-08-01 - v1.7.3 substitute PostScript name for fonts (LiberationSans for "Liberation Sans" and CourierNew for "Courier New") to address a flaw in "wkhtmltopdf" which rendered all text as bold. Changed "bigtitle" to "h1big"*/
 /* dk 2020-10-21 - v1.7.3a (unofficial for jadn, based on 1.7.3) update block quotes and code blocks */
+/* Heiko Theißen 2023-06-02 - v1.7.3b (unofficial for odata-data-aggregation-ext, based on v1.7.3a) include local font names "Liberation Sans" and "Courier New" */

 body {
     margin-left: 3pc;
     margin-right: 3pc;
-    font-family: LiberationSans, Arial, Helvetica, sans-serif;
+    font-family: LiberationSans, "Liberation Sans", Arial, Helvetica, sans-serif;
 	font-size:12pt;
 	line-height:1.2;
      }
@@ -26,10 +27,10 @@
 	 /* styles for section headings - levels 1-5 (maybe include heading1, etc. later) */
 h1{font-size:18pt}h2{font-size:14pt}h3{font-size:13pt}h4{font-size:12pt}h5{font-size:11pt}
 h1big{font-size: 24pt}
-h1,h2,h3,h4,h5,h1big{font-family: LiberationSans, Arial, Helvetica, sans-serif;font-weight: bold;margin:8pt 0;color: #446CAA}
+h1,h2,h3,h4,h5,h1big{font-family: LiberationSans, "Liberation Sans", Arial, Helvetica, sans-serif;font-weight: bold;margin:8pt 0;color: #446CAA}
 	/* style for h6, for use as Reference tag */
 h6{font-size:12pt; line-height:1.0}
-h6{font-family: LiberationSans, Arial, Helvetica, sans-serif;font-weight: bold;margin:0pt;}
+h6{font-family: LiberationSans, "Liberation Sans", Arial, Helvetica, sans-serif;font-weight: bold;margin:0pt;}
 	/* not needed - can just use brackets in the label itself */
 	/* h6::before {content: "["} */
 	/* h6::after {content: "]"} */
@@ -72,7 +73,7 @@
 }

 code,kbd,samp{
-    font-family:CourierNew, monospace;
+    font-family:CourierNew, "Courier New", monospace;
     white-space: pre-wrap;
     font-size: 10pt;
 }
```
