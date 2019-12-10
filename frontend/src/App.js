import React from 'react';
import logo from './logo.svg';
import './App.css';
import {MDBCard, MDBCardBody, MDBCardTitle, MDBCardText, MDBCardHeader, MDBBtn, MDBContainer, MDBRow, MDBCol, MDBProgress} from "mdbreact";
import * as d3 from 'd3';


class App extends React.Component {

    constructor(props, context) {
        super(props, context);
        this.state = {
            slider_value: 50,
            pos_rate: 25,
            neg_rate: 35,
            accuracy: 75,
            decided_rate: 0
        };
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event) {
        var prev = this.state.slider_value;
        var step = -1
        if (event.target.value > prev){
            step = 1
        }

        if (step > 0){
            this.setState(({pos_rate: this.state.pos_rate -1}))
        }
        if (step < 0){
            this.setState(({pos_rate: this.state.pos_rate +1}))
        }
        if (this.state.pos_rate <= 0){
            this.setState({pos_rate: 2})
        }

        if (step > 0){
            this.setState(({neg_rate: this.state.neg_rate -2}))
        }
        if (step < 0){
            this.setState(({neg_rate: this.state.neg_rate +2}))
        }
        if (this.state.neg_rate <= 0){
            this.setState({neg_rate: 2})
        }

        if (step > 0){
            this.setState({accuracy: this.state.accuracy +3})
            this.setState({decided_rate: this.state.decided_rate +2})
        }
        if (step < 0){
            this.setState({accuracy: this.state.accuracy -3})
            this.setState({decided_rate: this.state.decided_rate -2})
        }

        if (this.state.accuracy <= 60){
            this.setState({accuracy: 64})
            this.setState({decided_rate: 0})
        }

        if (this.state.accuracy >= 95){
            this.setState({accuracy: 89})
            this.setState({decided_rate: 70})
        }

        if (this.state.decided_rate <= -1){
            this.setState({decided_rate: 0})
        }




        // if (this.state.pos_rate < 25 || this.state.pos_rate >0){
        //     if (step > 0){
        //         this.setState({pos_rate:this.state.pos_rate-1});
        //     } else {
        //         this.setState({pos_rate:this.state.pos_rate+1});
        //     }
        // }

        // if (this.state.neg_rate < 25 || this.state.neg_rate >0){
        //     if (step > 0){
        //         this.setState({neg_rate:this.state.neg_rate-1});
        //     } else {
        //         this.setState({neg_rate:this.state.neg_rate+1});
        //     }
        // } else {
        //     if (step > 0){
        //         this.setState({neg_rate:0});
        //     } else {
        //         this.setState({neg_rate:25});
        //     }
        //
        // }


        // if (this.state.accuracy < 85 || this.state.accuracy >60){
        //     if (step > 0){
        //         this.setState({accuracy:this.state.accuracy+1});
        //     } else {
        //         this.setState({accuracy:this.state.accuracy-1});
        //     }
        // }
        // this.setState({decided_rate: (1/event.target.value)})
        this.setState({slider_value: event.target.value});
    }


    render() {
        return (
            <div className="App">
                <MDBRow>
                    <MDBCol >
                        <MDBContainer className="Panel overflow-auto">
                            <MDBCard style={{width: "22rem", marginTop: "1rem"}} className="card_style">
                                <MDBCardHeader color={"deep-purple darken-1"}>Featured</MDBCardHeader>
                                <MDBCardBody>
                                    <MDBCardTitle>Random Forest Classifier- Model 0</MDBCardTitle>
                                    <MDBCardText>
                                        Meta estimator that fits a number of decision tree classifiers on various sub-samples of the dataset
                                    </MDBCardText>
                                    <MDBBtn color="black">Select</MDBBtn>
                                </MDBCardBody>
                            </MDBCard>
                            <MDBCard style={{width: "22rem", marginTop: "1rem"}} className="card_style">
                                <MDBCardHeader color="deep-purple darken-1">Featured</MDBCardHeader>
                                <MDBCardBody>
                                    <MDBCardTitle>FC1 - Model A</MDBCardTitle>
                                    <MDBCardText>
                                        4 Layer NN - architecture, trained to 1000 epochs.
                                    </MDBCardText>
                                    <MDBBtn color="black">Select</MDBBtn>
                                </MDBCardBody>
                            </MDBCard>
                            <MDBCard style={{width: "22rem", marginTop: "1rem"}} className="card_style">
                                <MDBCardHeader color="deep-purple darken-1">Featured</MDBCardHeader>
                                <MDBCardBody>
                                    <MDBCardTitle>SVM - Model B</MDBCardTitle>
                                    <MDBCardText>
                                        Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.
                                    </MDBCardText>
                                    <MDBBtn color="black">Select</MDBBtn>
                                </MDBCardBody>
                            </MDBCard>
                            <MDBCard style={{width: "22rem", marginTop: "1rem"}} className="card_style">
                                <MDBCardHeader color="deep-purple darken-1">Featured</MDBCardHeader>
                                <MDBCardBody>
                                    <MDBCardTitle>Nearest Neighbor - Model C</MDBCardTitle>
                                    <MDBCardText>
                                        The principle behind nearest neighbor methods is to find a predefined number of training samples closest in distance to the new point,
                                        and predict the label from these.
                                    </MDBCardText>
                                    <MDBBtn color="black">Select</MDBBtn>
                                </MDBCardBody>
                            </MDBCard>
                            <MDBCard style={{width: "22rem", marginTop: "1rem"}} className="card_style">
                                <MDBCardHeader color="deep-purple darken-1">Featured</MDBCardHeader>
                                <MDBCardBody>
                                    <MDBCardTitle>Logisitic - Model D</MDBCardTitle>
                                    <MDBCardText>
                                        In this model, the probabilities describing the possible outcomes of a single trial are modeled using a logistic function.
                                    </MDBCardText>
                                    <MDBBtn color="black">Select</MDBBtn>
                                </MDBCardBody>
                            </MDBCard>
                        </MDBContainer>
                    </MDBCol>
                    <MDBCol className="custom_col">
                        <div className="my-5 slider_class">
                            <label htmlFor="customRange1" className="label_1">Model Requirements</label>
                            <input type="range" className="custom-range" id="customRange1" min={50} max={100} onChange={this.handleChange}/>
                        </div>
                        <div className="border_st">
                        <label className="label_2">
                            Confidence: {this.state.slider_value}%
                        </label>
                        </div>


                        <div className="space">

                        </div>

                        <MDBProgress material value={this.state.pos_rate} height="70px" width="600px" className="progress_bar">
                            False pos: {this.state.pos_rate}%
                        </MDBProgress>
                        <MDBProgress material value={this.state.neg_rate} height="70px" className="progress_bar">
                            False neg: {this.state.neg_rate}%
                        </MDBProgress>
                        <MDBProgress material value={this.state.accuracy} height="70px" className="progress_bar">
                            Accuracy: {this.state.accuracy}%
                        </MDBProgress>
                        <MDBProgress material value={this.state.decided_rate} height="70px" className="progress_bar">
                            unDecided_rate: {this.state.decided_rate}%
                        </MDBProgress>

                    </MDBCol>
                </MDBRow>


            </div>
        );
    }

}

export default App;
