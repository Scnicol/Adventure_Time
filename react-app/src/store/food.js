// ______ACTION_TYPES____________
const GET_FOOD = 'food/GET_FOOD'


// ______ACTIONS________________
const actionGetFood = (food) => ({
    type: GET_FOOD,
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

    }
}
