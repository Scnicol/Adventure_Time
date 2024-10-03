// __________ACTION_TYPES_____________
const GET_DIRECTIONS = 'directions/GET_DIRECTIONS'

// __________ACTIONS_________________
const actionGetDirections = (directions) => ({
    type: GET_DIRECTIONS,
    directions
})

//______THUNK_ACTIONS________________
export const getDirections = () => async dispatch => {
    const response = await fetch(`api/directions`);

    if (response.ok) {
        const data = await response.json();
        dispatch(actionGetDirections(data.directions))
    }
}

// ______CREATE_INITIAL_STATE_____________
const initialState = {};

// _____________DIRECTIONS_REDUCER______________
const directionReducer = (state = initialState, action) => {
    let newState = {};
    switch (action.type) {
        case GET_DIRECTIONS:
            let directionState = {};
            action.directions.forEach(direction => {
                directionState[direction.id] = direction;
            })
            return {
                ...state,
                ...directionState
            }
        default:
            return state;
    }
}

 export default directionReducer;
