require 'rspec'
require 'stringio'
require_relative '../lib/gravity'

describe 'load_data_file' do

  it 'should take a string as argument' do
    expect { load_data_file() }.to raise_error ArgumentError
  end

  #Detta test kan kommenteras bort om man inte vill testa 'Undantagshantering' på C- eller A-nivå
  it 'should raise ArgumentError with correct message if string is empty' do
    expect { load_data_file('') }.to raise_error ArgumentError, 'path must not be empty'
  end

  #Detta test kan kommenteras bort om man inte vill testa 'Undantagshantering' på C- eller A-nivå
  it 'should raise IOError with correct message if file does not exist' do
    expect { load_data_file('nonexisting.file') }.to raise_error IOError, 'file does not exist'
  end

  it 'should read the file and return an array of all rows in the file' do
    expect( load_data_file('spec/test.dat') ).to match_array ["Earth, 6367445, 5515\n", "Mars, 3386000, 3934\n", "Pluto, 1173000, 2050"]
  end

end

describe 'parse_lines' do

  before do
    @data = ["Earth, 6367445, 5515\n", "Mars, 3386000, 3934\n"]
  end

  it 'should take an array of data lines as argument' do
    expect { parse_lines() }.to raise_error ArgumentError
  end

  it 'should raise ArgumentError with correct error message if array is empty' do
    expect { parse_lines([])}.to raise_error ArgumentError, 'can not parse empty array'
  end

  it 'should return an array of hashes with the data from the array correctly formatted' do
    expect( parse_lines(@data) ).to match_array [ {:planet => 'Earth', :radius => 6367445, :density => 5515} , {:planet => 'Mars', :radius => 3386000, :density => 3934} ]
  end


end


describe 'calculate_weight' do

  before do
    @mercury = {:planet => 'Mercury', :radius => 2439700, :density => 5427}
    @imaginary_planet = { :planet => 'Braygh', :radius => 2818000, :density => 4358 }

  end


  it 'should take a mass and a hash of planetary information as arguments' do
    expect { calculate_weight() }.to raise_error ArgumentError
    expect { calculate_weight('oneargument') }.to raise_error ArgumentError
  end

  it 'should return a string of the planets name and the calculated weight' do
    calculate_weight(75, @mercury ).should == "Mercury: 277.442"
    calculate_weight(100, @imaginary_planet).should == "Braygh: 343.117"
  end

end

