// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage {
    uint256 public favoritenumber; // the public function makes the number visible

    //other visibility functions include private, internal amd external
    //how to write a storage function
    function store(uint256 _favoritenumber) public {
        favoritenumber = _favoritenumber;
    }

    // the view function is used to visualize things off the smartcontract which means it doesn't need any gas fee unlike other some functions
    function retrive() public view returns (uint256) {
        return favoritenumber;
    }

    // struct function can be used to create variable like function that stores multiple variables
    struct People {
        uint256 favorite;
        string name;
    }
    People[] public people; // this creates a dynamic array that stores people's name and dynamic numbers
    mapping(string => uint256) public nametofavnum;

    function addperson(string memory _name, uint256 _favoritenumber) public {
        // the memory keyword is used here because we are trying to specify that fact that the variables are temporal, until they are stored in the array
        people.push(People(_favoritenumber, _name));
        nametofavnum[_name] = _favoritenumber;
    }
}
