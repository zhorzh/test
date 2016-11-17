window.onload = function () {
  // fetch data from server
  fetch('/api/data')
    .then(function(response) {
      return response.json()
    })
    .then(function(json) {
      data = json['data']
      data = data.map(function(item) {
        return {date: d3.timeParse('%Y%m')(item[0]), price: item[1] }
      })

      // set chart dimensions
      svg = d3.select('svg'),
      margin = {top: 20, right: 20, bottom: 30, left: 50},
      width = +svg.attr('width') - margin.left - margin.right,
      height = +svg.attr('height') - margin.top - margin.bottom,

      // create chart
      g = svg.append('g').attr('transform', 'translate(' + margin.left + ',' + margin.top + ')')

      // set chart scales
      x = d3.scaleTime().rangeRound([0, width])
      y = d3.scaleLinear().rangeRound([height, 0])
      line = d3.line()
        .x(function(data) { return x(data.date) })
        .y(function(data) { return y(data.price) })
      x.domain(d3.extent(data, function(item) { return item.date }))
      y.domain(d3.extent(data, function(item) { return item.price }))

      // set chart styling
      g.append('g')
        .attr('class', 'axis axis--x')
        .attr('transform', 'translate(0,' + height + ')')
        .call(d3.axisBottom(x));
      g.append('g')
        .attr('class', 'axis axis--y')
        .call(d3.axisLeft(y))
        .append('text')
        .attr('fill', '#000')
        .attr('transform', 'rotate(-90)')
        .attr('y', 6)
        .attr('dy', '0.71em')
        .style('text-anchor', 'end')
        .text('Dollars per million BTU');
      g.append('path')
        .datum(data)
        .attr('class', 'line')
        .attr('d', line);
    }) 
}
