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
