pragma solidity ^0.5.0;

contract MapTest {
    uint private size = 0;

    mapping(uint => bool) private map;

    function inserirElemento(bool flag) public {
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
            if( map[i] == true ){
                j += 1;
            }
        }
        return j;
    }


}