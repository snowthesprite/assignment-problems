#for when you can't commit again VVV
#rm .git/index.lock
#python Assignment_82/test_82.py


ghc --make final_hs
./final_hs

echo 

g++ final_cpp.cpp -o final_cpp
./final_cpp

#python Quiz2.py