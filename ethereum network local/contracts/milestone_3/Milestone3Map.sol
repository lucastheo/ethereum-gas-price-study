pragma solidity ^0.5.0;

contract Milestone3Map {
    uint private size = 0;

    mapping(uint => int) private map;

    function inserirElemento(int flag) public {
        map[size] = flag;
        size++;
    }

    function contaElemento() public returns (uint){
        return size;
    }

    function percorre() public returns(uint)  {
        uint i;
        for( i = 0; i < size; i++ ){
            map[i];
        }
        return 0;
    }

    function percorreConta() public  returns(uint){
        uint i;
        uint j = 0;
        for( i = 0; i < size; i++ ){
            if( map[i] == 1 ){
                j += 1;
            }
        }
        return j;
    }


}
