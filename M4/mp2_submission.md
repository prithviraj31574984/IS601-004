<table><tr><td> <em>Assignment: </em> Mini Project 2_Advanced Calculator</td></tr>
<tr><td> <em>Student: </em> Prithvi Raj Goravi Dattathreya(pg79)</td></tr>
<tr><td> <em>Generated: </em> 3/23/2022 7:14:55 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/mini-project-2_advanced-calculator/grade/pg79" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Prepare your workspace</p>
<ol>
<li><code>git checkout dev</code></li>
<li><code>git pull origin dev</code></li>
<li><code>git checkout -b MP2-AdvCalc</code></li>
</ol>
<p>In this project, you&#39;ll decorate or extend one of the given MyCalc samples (do not edit MyCalc directly).
For every added calculation you&#39;ll need to provide a positive and negative test case.
<strong>Note:</strong> negative test cases will throw and capture exceptions to generate a positive test case
Negative test cases test for invalid input and/or invalid operations. These test cases will be via csv files as well 
(just like the changes to addition, subtraction, multiplication, division, square, and square root)</p>
<p>HINT 1: You can generate a normal distribution of random distribution of numbers with excel to use for your data:  Here (<a href="http://howtoexcel.org/statistics/normal-distribution/">http://howtoexcel.org/statistics/normal-distribution/</a>)</p>
<p>HINT 2: You can create another excel file that contains the answers to your calculations that you can use in your unit tests.</p>
<p><strong>Your program needs to additionally calculate the following:</strong></p>
<ol>
<li>Square</li>
<li>Square Root</li>
<li>Pick 5 from below<ul>
<li>Population Mean</li>
<li>Median</li>
<li>Mode</li>
<li>Population Standard Deviation</li>
<li>Variance of population proportion</li>
<li>Z-Score</li>
<li>Standardized score</li>
<li>Population Correlation Coefficient</li>
<li>Confidence Interval</li>
<li>Population Variance</li>
<li>P Value</li>
<li>Proportion</li>
<li>Sample Mean</li>
<li>Sample Standard Deviation</li>
<li>Variance of sample proportion</li>
</ul>
</li>
</ol>
<ul>
<li>You&#39;ll update your previous test cases to read from csv files for the input and output values.</li>
<li>Use the below csv files for your existing test cases of addition, subtraction, multiplication, and division.
As well as testing the new square and square root modifications.</li>
</ul>
<p><strong>Note</strong>: You may need to view the data via the &quot;Raw&quot; button on the gist.
<a href="https://gist.github.com/MattToegel/958ad17cc2c94337a5260126639eefbe">https://gist.github.com/MattToegel/958ad17cc2c94337a5260126639eefbe</a> </p>
<p>Once done do the following:</p>
<ol>
<li>Git add all changes (including the test case csv files)</li>
<li>Git commit with relevant messages</li>
<li>Git push origin MP2-AdvCalc</li>
<li>Create a Pull Request on Github to dev (keep it open)</li>
<li>Fill out the details here</li>
<li>Save and Generate the markdown (any changes require this step to be repeated)</li>
<li>Paste the content into a <code>mp2_submission.md</code> file</li>
<li>Git add/commit/push the submission file change</li>
<li>Complete the pull request merge</li>
<li>Create a new pull request from dev to prod and complete it</li>
<li>Navigate to prod branch&#39;s <code>mp2_submission.md</code> file and paste the direct link to Canvas</li>
</ol>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Added Functionality: Square </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159807971-30d26ba3-f65d-4dc4-9e81-9f81b34d0b64.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of square function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159808194-08a77134-828d-4318-92f2-36b32503f30c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>*** symbol is used for square<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the passing test cases from the csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159808654-29ee2939-496d-4742-b27f-f3c5330bcfed.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the passing square test case from the csv file<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Added Functionality: Square Root </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159807971-30d26ba3-f65d-4dc4-9e81-9f81b34d0b64.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>square root function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159808194-08a77134-828d-4318-92f2-36b32503f30c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>^^^ symbol is use for square root<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the passing test cases from the csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159808746-86b69325-cdc6-4098-a11d-b8bc388da547.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the passing square root test cases from the csv file<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Choice 1 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p>Mean which is used to find the average of a list of values<br>and used in  statistics and daily life.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159809155-8b6f018f-5ad7-49ea-8322-6a82393a383a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the mean choice we make while running the program and mainly<br>used for advanced calculations in the program<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159809348-f248999a-4983-4c02-b178-ad4b1481b194.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>mean function <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159809960-f617e060-2d01-4c10-889c-d30323cfac41.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of  mean positive test case execution<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of negative test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159810120-dfb21e31-be24-4a97-b79c-5f6d3ca7eccd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshot of mean negative test case execution<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Choice 2 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p>Median - In statistics and probability theory, the median is the value separating<br>the higher half from the lower half of a data sample, a population,<br>or a probability distribution. For a data set, it may be thought of<br>as &quot;the middle&quot; value<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159809155-8b6f018f-5ad7-49ea-8322-6a82393a383a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Median choice we make while running the program and mainly<br>used for advanced calculations in the program<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159809348-f248999a-4983-4c02-b178-ad4b1481b194.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>median function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159810301-be5d059b-24be-47a8-b648-f3d6115ceb7b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of median positive test case execution<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of negative test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159810413-5688b89c-e12b-4190-94ea-f6327bcd5923.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of median negative test case execution<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Choice 3 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p>mode -  The mode is the value that appears most often in<br>a set of data values. If X is a discrete random variable, the<br>mode is the value x at which the probability mass function takes its<br>maximum value. In other words, it is the value that is most likely<br>to be sampled<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159809155-8b6f018f-5ad7-49ea-8322-6a82393a383a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Mode choice we make while running the program and mainly<br>used for advanced calculations in the program<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159809348-f248999a-4983-4c02-b178-ad4b1481b194.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Mode function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159810653-58ce5f2d-9a35-4fd5-8029-bbc2de5634ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshot of mode positive test case execution<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of negative test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159810792-04273109-ab4d-4492-82d6-55178bfa9873.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshot of mode negativee test case execution<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Choice 4 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p>Population Standard deviation - In statistics, the standard deviation is a measure of<br>the amount of variation or dispersion of a set of values. A low<br>standard deviation indicates that the values tend to be close to the mean<br>of the set, while a high standard deviation indicates that the values are<br>spread out over a wider range.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159809155-8b6f018f-5ad7-49ea-8322-6a82393a383a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Population standard deviation  choice we make while running the<br>program and mainly used for advanced calculations in the program<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159809348-f248999a-4983-4c02-b178-ad4b1481b194.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Population standard deviation function <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159810976-7769f377-e4a8-40ca-868e-369498cb475f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshot of Population standard deviation positive test case execution<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159811177-8705fc5d-ac74-46ae-a96f-e2dd57e0e663.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Population standard deviation negative test case execution<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Choice 5 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p>Z-Score - In statistics, the standard score is the number of standard deviations<br>by which the value of a raw score is above or below the<br>mean value of what is being observed or measured. Raw scores above the<br>mean have positive standard scores, while those below the mean have negative standard<br>scores<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159809155-8b6f018f-5ad7-49ea-8322-6a82393a383a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Z-score  choice we make while running the program and<br>mainly used for advanced calculations in the program<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159809348-f248999a-4983-4c02-b178-ad4b1481b194.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Z-score function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159811438-233027b7-00d6-4b6b-82ae-4b139d4e8023.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Z-score positive test case execution<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/159811498-13528a61-4511-4b58-a9eb-a3daff4dcbcd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Z-score negative  test case execution<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Mention any difficulties and how you overcame them or what you learned during this mini project.</td></tr>
<tr><td> <em>Response:</em> <p>many difficulties were faced i did overcome through some online resources such as<br>stack over flow and some of the websites specified by professor<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Pull Request Link(s) for this project</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/prithviraj31574984/IS601-004/pull/11">https://github.com/prithviraj31574984/IS601-004/pull/11</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/mini-project-2_advanced-calculator/grade/pg79" target="_blank">Grading</a></td></tr></table>
