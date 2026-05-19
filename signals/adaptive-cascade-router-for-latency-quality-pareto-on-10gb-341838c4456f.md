# Adaptive Cascade Router for Latency-Quality Pareto on 10GB

Status: `useful_signal`
Project ID: `adaptive-cascade-router-for-latency-quality-pareto-on-10gb-341838c4456f`
Run ID: `adaptive-cascade-router-for-latency-quality-pareto-on-10gb-341838c4456f-20260517T204945810220+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ea6af4d7d3f3

## What looked useful

Adaptive empirical thresholding was slightly lower latency than a retrospective static threshold but missed the target quality floor; proportional adaptive thresholding met the floor only by over-escalating and adding about 19.9 ms mean latency versus the retrospective static control in the drift setting. Oracle routing showed large remaining headroom, so richer learned routers may still be worth testing.

## Boundaries and scale limits

Simulator-only proxy evidence; no real LLM outputs, no production traces, no server batching, no p95/p99 load test, and no direct 10GB/GB10 model-serving measurement.

## Claim scope

In a self-contained synthetic cascade benchmark with 50,000 requests x 20 seeds, nonstationary drift, confidence miscalibration, and a 0.89 quality floor, two simple adaptive scalar-confidence threshold controllers did not dominate a tuned static threshold on the latency-quality Pareto objective.

## Why it stopped

Medium synthetic proxy evidence was insufficient for a paper-positive claim and showed the tested adaptive controllers failed to beat a strong static control under the target latency-quality criterion.

## Recommended next action

Stop this run as a proxy early falsification of the tested adaptive threshold mechanisms; deepen only with real model outputs or a public dataset and a learned router compared against calibrated static thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-output learned cascade router versus calibrated static thresholds
- Success threshold: On held-out real-output data, learned routing must hit the selected quality floor in at least 95% of seeds/splits and reduce mean latency by at least 10% and p95 latency by at least 5% versus the best calibrated static threshold.
- Stop condition: Stop if the learned router misses the quality floor on more than 5% of held-out splits or fails to reduce both mean and p95 latency versus the static threshold baseline.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-cascade-router-for-latency-quality-pareto-on-10gb-341838c4456f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
