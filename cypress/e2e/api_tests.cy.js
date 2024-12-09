describe("API Tests", () => {
    it("should return prediction for valid input", () => {
        cy.request("POST", "/predict", { text: "I love Cypress!" }).then((response) => {
            expect(response.status).to.eq(200);
            expect(response.body[0]).to.have.property("label");
        });
    });

    it("should return error for empty input", () => {
        cy.request({
            method: "POST",
            url: "/predict",
            body: { text: "" },
            failOnStatusCode: false,
        }).then((response) => {
            expect(response.status).to.eq(400);
            expect(response.body).to.have.property("error");
        });
    });
});
