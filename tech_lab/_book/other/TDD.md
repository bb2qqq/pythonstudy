#测试驱动开发

### 步骤

1. 分析需求

2. 分解问题
化整为零

3. 明确目标(只关注眼前的小问题)
实现目标
检验目标


> 有明确的细分目标可以有助于将注意力集中到当前问题上

尽可能的打散需求，化整为零

### TDD Content
First fail the test cases. The idea is to ensure that the test really works and can catch an error.

Receiving the expected test results at each stage reinforces the programmer's mental model of the code, boosts confidence and increases productivity.

For TDD, a unit is most commonly defined as a class or group of related functions, often called a module. Keeping units relatively small is claimed to provide critical benefits, including:  
Reduced debugging effort – When test failures are detected, having smaller units aids in tracking down errors.  
Self-documenting tests – Small test cases have improved readability and facilitate rapid understandability.  

Effective layout of a test case ensures all required actions are completed, improves the readability of the test case, and smooths the flow of execution. Consistent structure helps in building a self-documenting test case. A commonly applied structure for test cases has (1) setup, (2) execution, (3) validation, and (4) cleanup.

Setup: Put the Unit Under Test (UUT) or the overall test system in the state needed to run the test.

Execution: Trigger/drive the UUT to perform the target behavior and capture all output, such as return values and output parameters. This step is usually very simple.

Validation: Ensure the results of the test are correct. These results may include explicit outputs captured during execution or state changes in the UUT & UAT.

Cleanup: Restore the UUT or the overall test system to the pre-test state. This restoration permits another test to execute immediately after this one.[8]

### Best Practice & Bad Practice
**Individual best practices[edit]**

This section contains instructions, advice, or how-to content. The purpose of Wikipedia is to present facts, not to train. Please help improve this article either by rewriting the how-to content or by moving it to Wikiversity, Wikibooks or Wikivoyage (May 2014)

This section is in a list format that may be better presented using prose. You can help by converting this section to prose, if appropriate. Editing help is available. (May 2014)  
Separate common set up and teardown logic into test support services utilized by the appropriate test cases.  
Keep each test oracle focused on only the results necessary to validate its test.
Design time-related tests to allow tolerance for execution in non-real time operating systems.   
The common practice of allowing a 5-10 percent margin for late execution reduces the potential number of false negatives in test execution.
Treat your test code with the same respect as your production code. It also must work correctly for both positive and negative cases, last a long time, and be readable and maintainable.
Get together with your team and review your tests and test practices to share effective techniques and catch bad habits. It may be helpful to review this section during your discussion.[11]

**§Practices to avoid, or "anti-patterns"[edit]**

Having test cases depend on system state manipulated from previously executed test cases.
Dependencies between test cases.   
A test suite where test cases are dependent upon each other is brittle and complex.   

Execution order should not be presumed. Basic refactoring of the initial test cases 
or structure of the UUT causes a spiral of increasingly pervasive impacts in associated tests.
Interdependent tests. Interdependent tests can cause cascading false negatives. A failure in an early test case breaks a later test case even if no actual fault exists in the UUT, increasing defect analysis and debug efforts.
Testing precise execution behavior timing or performance.
Building “all-knowing oracles.” An oracle that inspects more than necessary is more expensive and brittle over time. This very common error is dangerous because it causes a subtle but pervasive time sink across the complex project.[11]
Testing implementation details.
Slow running tests.



### TDD 和 Unittest 的区别

This is a differentiating feature of test-driven development versus writing unit tests after the code is written: it makes the developer focus on the requirements before writing the code, a subtle but important difference.


### 代码规范

缩进要尽可能的少，缩进越少，分散的精力越少。


### 其他
工具：stickles


### 练习

5个同品质卡合成一个卡

* 材料卡，5张
* 5张同品质
* 结果：1张卡
	* 集合中选一张卡（有两种集合）
		1. 普通集合：除特殊集合外的其他情况
			
		2. 特殊集合：  
			1.在特殊卡牌区间内
			2.特殊区间内可领奖励数不为0
			3.抽奖概率大于特殊集合领奖概率值 / 区间内最后zong抽奖
			
		
> 需要记录卡牌融合次数

> 其他可扩展性考虑：将来特殊奖励区间可能发生变动。 答案：设置版本号！
> 区间内设置多次抽奖怎么办？


合卡时从卡池选择一张卡作为结果
贺卡