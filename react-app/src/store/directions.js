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
