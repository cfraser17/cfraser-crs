describe('Test API GET and PUT', () => {
    it('First tests the GET API to confirm its greater than 0, the status is 200, and it is a string. Then, confirms that the PUT is increasing by 1', () => {
        let visitors
        
        cy.request('https://l7p4fn9k86.execute-api.us-east-1.amazonaws.com/Prod/get').then((response) => {
            expect(response.body.length).to.be.greaterThan(0)
            expect(response.status).to.equal(200)
            expect(response.body).to.be.a('string')
            visitors = response.body
        })
        cy.request('https://l7p4fn9k86.execute-api.us-east-1.amazonaws.com/Prod/put').then((response) => {
            expect(response.body.length).to.be.greaterThan(0)
            expect(response.status).to.equal(200)
            expect(response.body).to.be.a('string')
            expect(Number(response.body)).to.be.greaterThan(Number(visitors))
        })
    })
})