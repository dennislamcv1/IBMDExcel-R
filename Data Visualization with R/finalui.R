# Import the library
library(shiny)
library(tidyverse)

categorical_varibles = c('cyl', 'vs', 'am', 'gear', 'carb')

# Application Layout
shinyUI(fluidPage(
  br(),
  # TASK 1: Application title
  titlePanel(title = "Data Exploration Using Shiny"),
  # Define sidebar layout with sidebar panel and main panel
  sidebarLayout(
    sidebarPanel(
      # TASK 2: Add h3 and variable select inputs for continuous/categorical 
      h3('Explore mtcars'),
      varSelectInput("continuous_variable", 
                     "Select Continuous Variable",
                     data = select(mtcars, -categorical_varibles),
                     selected = "mpg"),
      varSelectInput("categorical_variable", 
                     "Select Categorical Variable",
                     data = mtcars[categorical_varibles],
                     selected = "cyl"),
      # TASK 3: Add numeric input for bins and radio buttons for fill
      h3("Histogram settings:"),
      numericInput("bins",
                  "Number of bins",
                  min = 2,
                  max = 20,
                  value = 10),
      radioButtons("hist_fill", 
                   "Histogram fill:", 
                   choices = c("default", "blue")),
      # TASK 4: Add variable map guide
      h4('Plot Variable Map Guide'),
      p('Miles/gallon = mpg', br(), 
        'Displacement (cu in.) = disp', br(),
        'Gross horsepower = hp', br(),
        'Rear axle ratio = drat', br(),
        'Weight (1000 lbs) = wt', br(),
        '1/4 mile time = qsec', br(),
        'Number of cylinders = cyl', br(),
        'Engine\n(0 = V-shaped, 1 = straight) = vs', br(), 
        'Transmission\n(0 = automatic, 1 = manual) = am', br(), 
        'Number of forward gears = gear', br(),
        'Number of carburetors = carb'
        )
    ),
    mainPanel(
      # TASK 5: Add three panels
      tabsetPanel(
        tabPanel(
          "Distribution of Numerical Variables",
          plotOutput("p1"),  # histogram
          plotOutput("p2")   # boxplot
        ),
        tabPanel(
          "Distribution of Categorical Variables",
          plotOutput("p3")  # bar chart
        ),
        tabPanel(
          "Plots for Observing Data Correlation",
          plotOutput("p4"))  # scatter plot
        )
      ),
    position = "right"
    )
))
