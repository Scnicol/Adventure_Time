// ___________ACTION_TYPES___________________
const GET_ADVENTURES = 'adventures/GET_ADVENTURES'
const GET_ADVENTURE_BY_ID = 'adventures/GET_ADVENTURE_BY_ID'

// ______ACTIONS____________
const actionGetAdventures = (adventures) => ({
    type: GET_ADVENTURES,
    adventures
})

const actionGetAdventureById = (adventure) => ({
    type: GET_ADVENTURE_BY_ID,
    adventure
})

//______THUNK_ACTIONS____________
export const getAdventures = () => async dispatch => {
    const response = await fetch(`/api/adventures`);

    if (response.ok) {
        const data = await response.json();
        dispatch(actionGetAdventures(data.adventures))
    }
}

export const getAdventureById = (adventureId) => async dispatch => {
    const response = await fetch(`/api/adventures/${adventureId}`)

    if (response.ok) {
        const adventure = await response.json();
        dispatch(actionGetAdventureById(adventure))
    }
}

// _____CREATE_INITIAL_STATE_________
const initialState = {};


// _________ADVENTURES_REDUCER_____________
const adventurReducer = (state = initialState, action) => {
    let newState = {};
    switch (action.type) {
        case GET_ADVENTURES:
            let adventuresState = {};
            action.adventures.forEach(adventure => {
                adventuresState[adventure.id] = user;
            })
            return {
                ...state,
                ...adventuresState
            }
        case GET_ADVENTURE_BY_ID:
            return {
                ...state,
                [action.adventure.id]: action.adventure
            }
    }
}
