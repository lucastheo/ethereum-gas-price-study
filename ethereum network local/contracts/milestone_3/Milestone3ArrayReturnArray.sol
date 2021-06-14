pragma solidity ^0.5.0;

contract Milestone3ArrayReturnArray {
    bool[] private array;

    function inserirElemento(bool flag) public {
        array.push(flag);
    }

    function contaElemento() public returns (uint){
        return array.length;
    }

    function percorre() public returns(uint)  {
        uint i;
        for( i = 0; i < array.length; i++ ){
            array[i];
        }
        return 0;
    }

    function percorreConta() public  returns(uint[] memory){
        uint i;
        uint j = 0;
        for( i = 0; i < array.length; i++ ){
            if( array[i] == true ){
                j += 1;
            }
        }

        uint[] memory array_return = new uint[](j);
        j = 0;
        for( i=0; i < array.length; i++ ){  
            if( array[i] == true ){
                array_return[j] = i;
                j += 1;
            }
        }
        return array_return;
    }

    function percorreContaList() public  returns(uint){
        uint i;
        uint j = 0;
        for( i = 0; i < array.length; i++ ){
            if( array[i] == true ){
                j+=1;
            }
        }
        
        return j;
    }

}