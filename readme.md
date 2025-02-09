#### Task 1

##### The Results:

| Terminal | Store | Max Flow |
| -------- | ----- | -------- |
| T1       | S1    | 15       |
| T1       | S2    | 10       |
| T1       | S3    | 20       |
| T1       | S4    | 15       |
| T1       | S5    | 10       |
| T1       | S6    | 20       |
| T1       | S7    | 15       |
| T1       | S8    | 15       |
| T1       | S9    | 10       |
| T1       | S10   | 0        |
| T1       | S11   | 0        |
| T1       | S12   | 0        |
| T1       | S13   | 0        |
| T1       | S14   | 0        |
| T2       | S1    | 0        |
| T2       | S2    | 0        |
| T2       | S3    | 0        |
| T2       | S4    | 10       |
| T2       | S5    | 10       |
| T2       | S6    | 10       |
| T2       | S7    | 15       |
| T2       | S8    | 15       |
| T2       | S9    | 10       |
| T2       | S10   | 20       |
| T2       | S11   | 10       |
| T2       | S12   | 15       |
| T2       | S13   | 5        |
| T2       | S14   | 10       |

##### Interpretation of the results

1. Terminal 1 provides the highest flow to stores like 1, 2, 3, and so on.
   Notable flows: Store 3 (20), Store 6 (20), and others between 10-15.
   Terminal 2 contributes the most to stores 10 (20), 12 (15), and others between 5-15.
   Terminal 1 delivers more overall flow to stores compared to Terminal 2, as Terminal 2
   primarily serves downstream stores not reachable by T1.
2. Routes from Terminal 1 to stores 10 - 14 show Max Flow = 0. Similarly, Terminal 2
   has no flow to Stores 1 - 3. These paths are likely constrained by intermediate
   bottlenecks in the warehouses or due to routing inefficiencies.
   The total network flow is restricted because certain stores are not served by one
   terminal, necessitating a heavier reliance on the other.
3. Stores receiving the least or no flow:
   From Terminal 1: 10 - 14 (all with Max Flow = 0).
   From Terminal 2: 1 - 3 (all with Max Flow = 0).
   Potential Improvements:
   Increasing the capacities between Terminal 1 and warehouses like Warehouse 3 or
   adding direct links to Warehouse 4.
   Enhancing capacities between Terminal 2 and Warehouse 1 or 3 for upstream delivery.
4. Bottlenecks:
   - Capacity constraints between terminals and warehouses (e.g., Terminal 1 → Warehouse 3, Terminal 2 → Warehouse 2).
   - Overloaded warehouses, such as Warehouses 3 and 4, unable to distribute goods to all connected stores.
5. Suggestions for Improvement:
   - Add redundancy by connecting Terminal 1 directly to downstream warehouses like Warehouse 4.
   - Increase capacity on key links, such as Warehouse 3 → Stores 7 - 9 and Warehouse 4 → Stores 10 - 14.
   - Introduce alternate paths or inter-terminal transfers to balance the load.

##### Conclusion

The current logistics network is functional but exhibits bottlenecks and unused
capacity in several areas. Targeted capacity increases and additional routing could
significantly enhance the overall flow and balance the supply to under-served stores.

#### Task 2

Install the requirements:

```shell
pip install -r requirements.txt
```

Run the Benchmark:

```shell
python3 -m unittest ./test_data_storage.py
```

Sample result:

```
Total range_query time for OOBTree: 4.757088 seconds
Total range_query time for Dict: 1.290547 seconds
```

##### Conclusion

1. For range queries based on value filtering, dict provides better performance
   due to its simpler structure.
2. The sorted key advantage of OOBTree is irrelevant here because filtering is
   based on values (Price), not keys.
