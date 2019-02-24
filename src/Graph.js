import React, { Component } from 'react';
import { ParallelCoordinates } from 'react-vis';

let data = [
    {
        name: 'Honda',
        mileage: 8,
        price: 6,
        safety: 9,
        performance: 6,
        interior: 3,
        warranty: 9,
        style: {
          strokeWidth: 3,
          strokeDasharray: '2, 2'
        }
    }
]

let domains = [
    {
        name: "test",
        getValue: x => x.warranty,
        domain: [0, 10],
        tickFormat: x => x
    },
    {
        name: "test2",
        getValue: x => x.performance,
        domain: [0, 10],
        tickFormat: x => x
    }
]


class Graph extends Component {
    render() {
        return (
            <div>
                <ParallelCoordinates data={data}
                domains={domains}
                height={350}
                width={600}/>
            </div>
        )
    }
}

export default Graph;