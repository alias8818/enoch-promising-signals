# Speculative Decoding with Quantized Residual Draft Models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-with-quantized-residual-draft-models-dadbe4796592`
Run ID: `speculative-decoding-with-quantized-residual-draft-models-dadbe4796592-20260611T175659101314+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/749fa37361d0

## What looked useful

Residual int8 reduced mean target KL by 3.76% and mean target calls per emitted token by 4.99% versus the plain draft across seeds 7, 11, and 13, while using 1,360 int8 residual weight bytes plus scales. However, one seed regressed in speculative efficiency, so the int8 acceptance claim is mixed rather than supported.

## Boundaries and scale limits

No real tokenizer corpus, GPT-2-small-class model, production serving kernel, quantization-aware training, or end-to-end latency benchmark was tested. Evidence is bounded to tiny local models and sampled speculative acceptance accounting with gamma=4.

## Claim scope

Toy character-level Transformer probe on a deterministic structured corpus: a low-rank residual draft correction trained against target logits improved target KL after int8 post-training quantization, and improved aggregate speculative target-call efficiency versus a plain draft across three seeds, but acceptance was not consistently improved in every seed.

## Why it stopped

This run is a bounded toy useful-signal result, not full validation: the mechanism improved KL consistently but quantized residual speculative acceptance was mixed across seeds.

## Recommended next action

Run a bounded deepen test on a GPT-2-small-class tokenizer benchmark with fixed proposal traces, a parameter-matched draft baseline, and repeated seeds; stop if int8 residual drafts fail to improve target-call efficiency in at least 4 of 5 seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class fixed-trace test for quantized residual speculative drafts
- Success threshold: Residual int8 improves target calls per emitted token by at least 5% versus the plain draft in at least 4 of 5 seeds, with no more than 5% additional draft storage and no KL regression versus plain draft.
- Stop condition: Stop as a negative if residual int8 does not improve target-call efficiency in at least 4 of 5 seeds or if measured residual overhead removes the expected speculative decoding benefit.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-quantized-residual-draft-models-dadbe4796592`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
