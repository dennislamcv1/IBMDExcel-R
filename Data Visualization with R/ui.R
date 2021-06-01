# Import the library
library(shiny)

shinyUI(
  fluidPage(
    # TASK 1: Application title
    titlePanel("Motor Trend Car Road Tests Data"),
    # Define vertical layout with main panel on top and slider below
    verticalLayout(
      # TASK 2: Add plot output
      plotOutput("histPlot"),
      # TASK 3: Add slider input
      sliderInput(
        inputId = "bins",
        label = "Number of bins:",
        min = 1,
        max = 10,
        value = 5
      )
    )
  )
) 