/**
 * Copy paste in the console, then restart the game (space bar)
 *
 * Greedy Algorithm for : http://gabrielecirulli.github.io/2048/
 * Plays the game using a naive greedy method. i.e. Local maximum
 *
 * Azaan
 */
(function () {
    var __restart = GameManager.prototype.restart;
    var GM;
  
    GameManager.prototype.restart = function () {
      GM = this;
      __restart.bind(this)();
  
      var strategy = new GreedyStrategy(GM);
      console.log('hi');
      setTimeout(function () {
        strategy.play(window.DELAY || 100);
      }, 0);
    };
  
    function GreedyStrategy(gm) {
      this.gm = gm;
    }
  
    GreedyStrategy.prototype.cloneGrid = function () {
      function cloneTile(tile) {
        var t = new Tile({x: tile.x, y: tile.y}, tile.value);
        t.previousPosition = tile.previousPosition;
        t.mergedFrom = tile.mergedFrom;
        return t;
      }
  
      var arr = [], i, j, len, len2;
      for (i = 0, len = this.gm.grid.size; i < len; i++) {
        arr[i] = this.gm.grid.cells[i].slice();
  
        for (j = 0, len2 = arr[i].length; j < len2; j++) {
          if (arr[i][j] !== null) {
            arr[i][j] = cloneTile(arr[i][j]);
          }
        }
      }
  
      var g = new Grid(this.gm.grid.size);
      g.cells = arr;
      return g;
    };
  
    GreedyStrategy.prototype.freeze = function () {
      this._grid = this.gm.grid;
      this._act = this.gm.actuator;
      this._score = this.gm.score;
      this._over = this.gm.over;
      this._won = this.gm.won;
  
      this.gm.actuator = undefined;
      this.gm.grid = this.cloneGrid();
    };
  
    GreedyStrategy.prototype.restore = function () {
      this.gm.grid = this._grid;
      this.gm.actuator = this._act;
      this.gm.score = this._score;
      this.gm.won = this._won;
      this.gm.over = this._over;
    };
  
    GreedyStrategy.prototype.step = function () {
      var scores = [], i;
  
      for (i = 0; i < 4; i++) {
        this.freeze();
  
        try {
          this.gm.move(i);
          scores.push(-Infinity);
        } catch (e) {
          // add score only if something moved
          scores.push(this.gm.score);
        }
  
  
        this.restore();
      }
  
      return scores;
    };
  
    GreedyStrategy.prototype.play = function (d) {
      var self = this, next;
      var delay = d || 0;
  
      next = function () {
        var maxI = 0, scores;
  
        scores = self.step();
        for (i = 0; i < 4; i++) {
          if (scores[i] > scores[0])
            maxI = i;
        }
  
        console.log(scores);
        window.requestAnimationFrame(function () {
          self.gm.move(maxI);
  
          if (!self.gm.over) {
            setTimeout(next, delay);
          }
        });
      };
  
      next();
    };
  
    new GameManager(4, KeyboardInputManager, HTMLActuator);
  })();