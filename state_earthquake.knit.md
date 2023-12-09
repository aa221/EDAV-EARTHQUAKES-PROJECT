
<!-- rnb-text-begin -->

---
title: "R Notebook"
output: html_notebook
---


<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG5zdGF0ZV9lYXJ0aHF1YWtlcyA8LSByZWFkLmNzdihcIi9Vc2Vycy9hZGVsYWJkYWxsYS9EZXNrdG9wL2VhcnRocXVha2VzX2J5X3N0YXRlLmNzdlwiKVxuXG5cblxuXG5gYGAifQ== -->

```r

state_earthquakes <- read.csv("/Users/adelabdalla/Desktop/earthquakes_by_state.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->




<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuaW5zdGFsbC5wYWNrYWdlcygnZHBseXInKVxuYGBgIn0= -->

```r
install.packages('dplyr')
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiRXJyb3IgaW4gaW5zdGFsbC5wYWNrYWdlcyA6IFVwZGF0aW5nIGxvYWRlZCBwYWNrYWdlc1xuIn0= -->

```
Error in install.packages : Updating loaded packages
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxubGlicmFyeSgnb3Blbnhsc3gnKVxuXG4jIEFzc3VtaW5nIHlvdSBoYXZlIGFuIEV4Y2VsIGZpbGUgbmFtZWQgXCJ5b3VyX2RhdGEueGxzeFwiIGluIHlvdXIgd29ya2luZyBkaXJlY3RvcnlcbnN0YXRlX3BvcCA8LSByZWFkLnhsc3goXCIvVXNlcnMvYWRlbGFiZGFsbGEvRGVza3RvcC9zdGF0ZV9wb3AueGxzeFwiKVxuXG4jIFRoZSB0aGlyZCByb3cgaGFzIHRoZSBjb2x1bW4gbmFtZXNcbmxpYnJhcnkoamFuaXRvcilcbmxpYnJhcnkoZHBseXIpXG5cblxuc3RhdGVfcG9wIDwtIHN0YXRlX3BvcCAlPiVcbiAgcm93X3RvX25hbWVzKHJvd19udW1iZXIgPSAzKSAlPiVcbiAgY2xlYW5fbmFtZXMoKVxuXG5zdGF0ZV9wb3AgJT4lXG4gIHJlbmFtZShhY3Jvc3MoMSwgfiBcIlN0YXRlXCIpKVxuYGBgIn0= -->

```r
library('openxlsx')

# Assuming you have an Excel file named "your_data.xlsx" in your working directory
state_pop <- read.xlsx("/Users/adelabdalla/Desktop/state_pop.xlsx")

# The third row has the column names
library(janitor)
library(dplyr)


state_pop <- state_pop %>%
  row_to_names(row_number = 3) %>%
  clean_names()

state_pop %>%
  rename(across(1, ~ "State"))
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiRXJyb3IgaW4gYHJlbmFtZSgpYDpcbiEgUHJvYmxlbSB3aGlsZSBldmFsdWF0aW5nIGBhY3Jvc3MoMSwgflwiU3RhdGVcIilgLlxuQ2F1c2VkIGJ5IGVycm9yIGluIGBhY3Jvc3MoKWA6XG4hIE11c3Qgb25seSBiZSB1c2VkIGluc2lkZSBkYXRhLW1hc2tpbmcgdmVyYnMgbGlrZSBgbXV0YXRlKClgLCBgZmlsdGVyKClgLCBhbmRcbiAgYGdyb3VwX2J5KClgLlxuQmFja3RyYWNlOlxuICAxLiBzdGF0ZV9wb3AgJT4lIHJlbmFtZShhY3Jvc3MoMSwgflwiU3RhdGVcIikpXG4gMjQuIGRwbHlyOjphY3Jvc3MoMSwgflwiU3RhdGVcIilcbiJ9 -->

```
Error in `rename()`:
! Problem while evaluating `across(1, ~"State")`.
Caused by error in `across()`:
! Must only be used inside data-masking verbs like `mutate()`, `filter()`, and
  `group_by()`.
Backtrace:
  1. state_pop %>% rename(across(1, ~"State"))
 24. dplyr::across(1, ~"State")
```



<!-- rnb-output-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->

