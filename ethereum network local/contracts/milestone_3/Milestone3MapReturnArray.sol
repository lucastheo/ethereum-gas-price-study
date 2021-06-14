pragma solidity ^0.5.0;

contract Milestone3MapReturnArray {
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

    function percorreConta() public  returns(uint[] memory ){
        uint i;
        uint j = 0;
        for( i = 0; i < size; i++ ){
            if( map[i] == true ){
                j += 1;
            }
        }

        uint[] memory map_return = new uint[](j);
        j = 0;
        for( i=0; i < size; i++ ){
            if( map[i] == true ){
                map_return[j] = i;
                j += 1;
            }
        }
        return map_return;
        
    }

}