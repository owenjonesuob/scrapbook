library(dplyr)
library(ggplot2)

mtcars %>%
  mutate(cyl = paste0(
    stringr::str_pad(
      c("", "A", "AA", "AAA")[cyl/2],
      pad = "\u2007", # <<-- "figure space"
      width = 4,
      side = "right"
    ),
    "(", cyl, ")"
  )) %>%
  ggplot(aes(wt, mpg, colour = cyl)) + geom_point()
