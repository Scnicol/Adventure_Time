// ______ACTION_TYPES____________
const GET_FOOD = 'food/GET_FOOD'
const GET_FOOD_BY_ID = 'food/GET_FOOD_BY_ID'


// ______ACTIONS________________
const actionGetFood = (food) => ({
    type: GET_FOOD,
    food
})

const actionGetFoodById = (food) => ({
    type: GET_FOOD_BY_ID,
    food
})


// --------THUNK_ACTIONS____________
export const getFood = () => async dispatch => {
    const response = await fetch(`/api/food`);

    if (response.ok) {
        const data = await response.json();
        dispatch(actionGetFood(data.food))
    }
}

export const getFoodById = (foodId) => async dispatch => {
    const response = await fetch(`/api/food/${foodId}`)

    if (response.ok) {
        const food = await response.json();
        dispatch(actionGetFoodById(food))
    }
}


// ___________CREATE_INITIAL_STATE______________
const initialState = {};

// ____________FOOD_REDUCER______________________
const foodReducer = (state = initialState, action) => {
    let newState = {};
    switch (action.type) {
        case GET_FOOD:
            let foodState = {};
            action.food.forEach(food => {
                foodState[food.id] = food;
            })
        default:
            return state;
    }
}


export default foodReducer;
