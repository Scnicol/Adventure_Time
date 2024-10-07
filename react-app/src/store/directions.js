// __________ACTION_TYPES_____________
const GET_DIRECTIONS = 'directions/GET_DIRECTIONS'
const GET_DIRECTION_BY_ID = 'directions/GET_DIRECTION_BY_ID'

// __________ACTIONS_________________
const actionGetDirections = (directions) => ({
    type: GET_DIRECTIONS,
    directions
})

const actionGetDirectionByID = (directions) => ({
    type: GET_DIRECTION_BY_ID,
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

export const getDirectionById = (directionId) => async dispatch => {
    const response = await fetch(`/api/challenges/${directionId}`)

    if (response.ok) {
        const direction = await response.json();
        dispatch(actionGetDirectionByID(direction))
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
        case GET_DIRECTION_BY_ID:
            return {
            ...state,
            [action.direction.id]: action.direction
            }

        default:
            return state;
    }
}

 export default directionReducer;
