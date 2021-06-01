library(shiny)
library(ggplot2)

# Define server logic required to draw a histogram
shinyServer(
  function(input, output) {
    output$histPlot <- renderPlot({
      # Draw the histogram with the specified  bins, input$bins
      ggplot(mtcars, aes(x = mpg)) +
        geom_histogram(bins = input$bins) + 
        labs(x = "Miles/gallon",
             y = "Frequency",
             title = "Histogram of miles/gallon of cars"
        ) +
        theme(text = element_text(size = 20))
    })
  }
)
