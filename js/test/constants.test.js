import { expect } from 'chai'
import { DIRECTION_COORDINATES } from '../src/constants'

describe('Constants', () => {
    it('returns the first element as [1, 0, -1]', () => {
        expect(DIRECTION_COORDINATES[0]).to.be.an('array').that.deep.equals([1, 0, -1])
    })
})



