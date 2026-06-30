# Medium GPT-2 INT2 Residual Channel Preservation With Realistic Quantization Baselines

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `medium-gpt-2-int2-residual-channel-preservation-with-reali-672c66cd3f`
Run ID: `medium-gpt-2-int2-residual-channel-preservation-with-reali-672c66cd3f-20260611T121052902930+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Residual Channel Preservation in INT2 Quantization: enoch://control-plane/projects/residual-channel-preservation-in-int2-quantization-b5e66ee85e13/runs/residual-channel-preservation-in-int2-quantization-b5e66ee85e13-20260611T115328298341+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/749fa37361d0

## What looked useful

Primary GPT-2-medium run: FP16 PPL 45.50, INT2 groupwise RTN PPL 13361.39, INT2 random-preserve PPL 12303.35, INT2 residual-channel-preserve PPL 3548.01. RCP improved perplexity by 73.45% relative to INT2 RTN and beat random preservation under the same 2% preserve fraction.

## Boundaries and scale limits

Single pretrained GPT-2-medium model, one dataset slice, 16,256 evaluated tokens in the primary run, one preserve fraction, one group size, one random-control seed, no optimized kernel, no full benchmark suite, no storage-normalized mixed-precision baseline beyond equal preserved-channel random control.

## Claim scope

On a bounded GPT-2-medium Wikitext-2 slice, preserving 2% calibration-selected residual/input channels in full precision while applying groupwise affine INT2 projection-weight quantization substantially reduced perplexity damage versus groupwise INT2 RTN and beat a random-preservation control.

## Why it stopped

Tier 1 direct test succeeded as useful mechanism evidence, but the evidence is too narrow for publication readiness.

## Recommended next action

Run a bounded robustness follow-up on GPT-2-medium/full Wikitext-2 with multiple preserve fractions, random seeds, group sizes, and storage-normalized mixed-precision baselines before considering a paper gate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-medium INT2 residual channel preservation robustness and storage-normalized baselines
- Success threshold: RCP must reduce perplexity damage by at least 20% versus INT2 RTN, beat all random-preservation controls, and beat or match the storage-normalized mixed-precision baseline at the same effective bit budget.
- Stop condition: Stop if RCP fails to beat random preservation in two or more preserve-fraction settings or cannot beat storage-normalized mixed precision on the primary held-out perplexity metric.

## Evidence references

- Artifact root: `<local-path>/projects/medium-gpt-2-int2-residual-channel-preservation-with-reali-672c66cd3f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
