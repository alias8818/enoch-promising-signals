# Cost-Aware Local Cascade Router: Tiered Routing Between 1B and 8B on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cost-aware-local-cascade-router-tiered-routing-between-1b-and-8b-on-gb10-9d4b6b7034f5`
Run ID: `cost-aware-local-cascade-router-tiered-routing-between-1b-and-8b-on-gb10-9d4b6b7034f5-20260619T120852211231+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d2902e151206

## What looked useful

Small baseline was 48.75% accurate at 22.4% of large forward cost; large baseline was 70.00% accurate. The best confidence router under always-large cost reached 68.75% accuracy at 98.67% of large cost. Matching large accuracy required 101.17% of large cost. An oracle route using correctness labels would reach 80.00% accuracy at 53.67% of large cost, indicating complementarity but not a deployable router.

## Boundaries and scale limits

Single benchmark slice, 80 examples, next-token multiple-choice scoring only, no learned router, no free-form generation, no batching or production serving stack, and forward-pass seconds used as a local cost proxy rather than measured energy or dollars.

## Claim scope

On 80 cached MMLU validation examples using GB10 CUDA inference with Llama-3.2-1B-Instruct as the small tier and Llama-3.1-8B-Instruct as the large tier, a naive small-model confidence router did not match always-8B accuracy while reducing expected forward-pass cost. It did show model complementarity and an oracle ceiling suggesting a better router may be worthwhile.

## Why it stopped

The direct medium proxy falsified the naive confidence-router version of the hypothesis: preserving always-8B accuracy required routing enough requests that expected forward-pass cost exceeded always-8B. This is not a full production-serving validation.

## Recommended next action

Run one bounded follow-up that trains/calibrates a router on small-model signals using a train/held-out split, and require at least 10% measured forward-cost reduction at no accuracy loss versus always-8B before considering deeper validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out learned router for 1B-to-8B local cascades
- Success threshold: On held-out examples, learned/calibrated router accuracy is at least always-8B accuracy and expected measured forward or serving cost is at least 10% lower than always-8B.
- Stop condition: Stop if the best held-out router that matches always-8B accuracy saves less than 5% measured cost, or if any apparent saving disappears under bootstrap resampling or a second benchmark slice.

## Evidence references

- Artifact root: `<local-path>/projects/cost-aware-local-cascade-router-tiered-routing-between-1b-and-8b-on-gb10-9d4b6b7034f5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
