// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

interface IPyth {
    struct Price {
        int64 price;
        uint64 conf;
        int32 expo;
        uint publishTime;
    }

    function getUpdateFee(bytes[] calldata updateData) external view returns (uint256);
    function updatePriceFeeds(bytes[] calldata updateData) external payable;
    function getPrice(bytes32 id) external view returns (Price memory);
}

contract AIOracleIntegration {
    IPyth public pyth;
    bytes32 public priceFeedId;
    uint256 public latestAISignal;

    event AISignalUpdated(uint256 newSignal);

    constructor(address _pythContract, bytes32 _priceFeedId) {
        pyth = IPyth(_pythContract);
        priceFeedId = _priceFeedId;
    }

    function fetchAISignal(bytes[] calldata priceUpdateData) external payable {
        uint256 fee = pyth.getUpdateFee(priceUpdateData);
        pyth.updatePriceFeeds{value: fee}(priceUpdateData);

        IPyth.Price memory price = pyth.getPrice(priceFeedId);
        require(price.price > 0, "Price must be positive");

        latestAISignal = uint256(uint64(price.price));
        emit AISignalUpdated(latestAISignal);
    }

    function getAISignal() external view returns (uint256) {
        return latestAISignal;
    }
}

