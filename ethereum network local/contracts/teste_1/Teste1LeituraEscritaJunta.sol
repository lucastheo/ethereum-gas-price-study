
pragma solidity ^0.5.0;

contract Teste1EscritaLeituraEscritaJunta {
  uint public taskCount = 0;
  
  struct Task {
    uint id;
    string content;
    uint256 value;
    bool completed;
  }

  mapping(uint => Task) public tasks;

  event TaskCreated(
    uint id,
    string content,
    bool completed
  );

  event TaskCompleted(
    uint id,
    bool completed
  );

  constructor() public {
    createTask2("Check out dappuniversity.com");
  }

  function createTask2(string memory _content) public {
    taskCount ++;

    uint256 j = 0;
    for (uint i=0; i<taskCount; i++) {
      if(tasks[i].id % 2 == 0){
        j +=1;
      } 
    }

    tasks[taskCount] = Task(taskCount, _content, j , false );
    emit TaskCreated(taskCount, _content, false);
  }

}