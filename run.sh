# declare -A TASK=(["SBI"]="RunPipeline")
# # echo ${TASK["SBI"]}
# echo $NAMESPACE
# export PIPELINE="${1}"
# echo $PIPELINE
# echo ${NAMESPACE}.${TASK["${PIPELINE}"]}


# declare namespace_math_value=42
# declare namespace_string_text="Hello"

# # Use declare -n to reference a variable dynamically
# namespace="namespace_math"
# declare -n var="${namespace}_value"
# echo "Math Value: $var"  # Output: Math Value: 42


#sh run.sh

declare -A TASK=(["SBI"]="RunPipeline" ["SBI2"]="RunPipeline2")
export A="${1}"
echo " running $TASK["${A}"] "

# fruits=("apple" "banana" "cherry")

# # Access elements
# echo ${fruits[0]}  # Output: apple
# echo ${fruits[1]}  # Output: banana

# # Access all elements
# echo ${fruits[@]}  # Output: apple banana cherry

# # Get the length of the array
# echo ${#fruits[@]}  # Output: 3

# # Loop through the array
# for fruit in "${fruits[@]}"; do
#     echo "$fruit"
# done



# # Add key-value pairs
# my_array["name"]="John"
# my_array["age"]="30"
# my_array["city"]="New York"

# # Access elements
# echo "Name: ${my_array["name"]}"   # Output: Name: John
# echo "Age: ${my_array["age"]}"     # Output: Age: 30
# echo "City: ${my_array["city"]}"   # Output: City: New York




# Access All Keys:
# bash
# Copy code
# echo "Keys: ${!my_array[@]}"   # Output: Keys: name age city
# Access All Values:
# bash
# Copy code
# echo "Values: ${my_array[@]}"  # Output: Values: John 30 New York
