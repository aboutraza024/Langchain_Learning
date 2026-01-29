from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
import os
load_dotenv()

model1=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=1,api_key=os.getenv("GOOGLE_GEMINI_KEY1"))
model2=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=1,api_key=os.getenv("GOOGLE_GEMINI_KEY2"))

prompt1=PromptTemplate(template='Create very simple and clear notes on this {text}', input_variables=['text'])
prompt2=PromptTemplate(template='Create a quiz on this {text}', input_variables=['text'])
prompt3=PromptTemplate(template='combine both documents on -> {notes} and ->{quiz}', input_variables=['text'])

parser=StrOutputParser()
parallel_chain=RunnableParallel({
    'notes': prompt1|model1|parser,
    'quiz': prompt2|model2|parser
})

text="""Understanding Linear Regression: A Comprehensive GuideLinear Regression is one of the most fundamental and widely used 
algorithms in statistics and machine learning. At its core, it is a method used to model the relationship between a dependent variable (the outcome you want to predict) and one or more independent variables (the factors that influence that outcome).1. The Core ConceptThe goal of linear regression is to find a mathematical equation that best describes the connection between variables. If we have only one independent variable, it is called Simple Linear Regression. If we have multiple independent variables, it is known as Multiple Linear Regression.The relationship is expressed through the equation of a straight line:$$y = \beta_0 + \beta_1x + \epsilon$$$y$: The dependent variable (Target).$x$: The independent variable (Predictor).$\beta_0$: The Y-intercept (the value of $y$ when $x = 0$).$\beta_1$: The slope (the change in $y$ for every one-unit change in $x$).$\epsilon$: The error term (the difference between actual data points and the predicted line).2. How it Works: The Line of Best FitIn a scatter plot of data points, there are infinite lines you could draw. Linear regression uses a method called Ordinary Least Squares (OLS) to find the "best" one.The "best fit" is the line that minimizes the sum of the squares of the vertical deviations (called residuals) between each data point and the line. By squaring these distances, we ensure that positive and negative errors don't cancel each other out and that larger errors are penalized more heavily.3. Key AssumptionsFor a linear regression model to provide reliable predictions, several assumptions must hold true:Linearity: The relationship between the independent and dependent variables must be linear.Independence: Observations must be independent of each other.Homoscedasticity: The variance of residual errors should be constant across all levels of the independent variables.Normality: For any fixed value of $x$, $y$ is normally distributed (specifically, the error terms should follow a normal distribution).4. Evaluating the ModelOnce a model is built, we need to know how well it performs. Common metrics include:R-Squared ($R^2$): Also known as the "Coefficient of Determination," it measures the proportion of variance in the dependent variable that is predictable from the independent variables. An $R^2$ of 1.0 means the model explains all the variability.Mean Absolute Error (MAE): The average of the absolute differences between predicted and actual values.Mean Squared Error (MSE): The average of the squared differences. This is sensitive to outliers.Root Mean Squared Error (RMSE): The square root of MSE, which brings the error metric back into the same units as the dependent variable.5. Practical Implementation (Python Example)Given your interest in Python and data analysis, here is how you would typically implement a linear regression model using the scikit-learn library:Pythonimport numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample data: Years of Experience vs Salary
X = np.array([[1], [2], [3], [4], [5]]) 
y = np.array([45000, 50000, 60000, 80000, 110000])

# Initialize and train the model
model = LinearRegression()
model.fit(X, y)

# Predict values
predictions = model.predict(X)

# Output coefficients
print(f"Intercept: {model.intercept_}")
print(f"Slope: {model.coef_[0]}")
6. Real-World ApplicationsLinear regression is highly versatile and appears in various industries:Finance: Predicting stock prices or identifying trends in consumer spending.Real Estate: Estimating house prices based on square footage, location, and age.Healthcare: Modeling the impact of drug dosage on blood pressure.Marketing: Calculating the Return on Investment (ROI) of advertising spend across different channels.7. LimitationsWhile powerful, linear regression isn't a "silver bullet." It struggles with:Non-linear relationships: If the data follows a curve (like exponential growth), a straight line will yield poor results.Outliers: A single extreme data point can significantly "pull" the line away from the rest of the data.Overfitting: In multiple regression, adding too many variables can make the model "memorize" the noise rather than learning the trend."""

result=parallel_chain.invoke({'text':text})

merge_chain=prompt3|model1|parser

final_chain=parallel_chain|merge_chain


output=final_chain.invoke({'text':text})
# print(output)

print(final_chain.get_graph().print_ascii())  # to visualize the chain structure