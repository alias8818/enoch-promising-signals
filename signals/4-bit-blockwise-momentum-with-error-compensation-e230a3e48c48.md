# 4-Bit Blockwise Momentum with Error Compensation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-blockwise-momentum-with-error-compensation-e230a3e48c48`
Run ID: `4-bit-blockwise-momentum-with-error-compensation-e230a3e48c48-20260526T100621200136+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1a4d425f5a56

## What looked useful

Error compensation appears mechanistically effective for convergence, but naive FP32 residual feedback defeats the memory-saving purpose of 4-bit momentum. Future work should test compressed residual feedback before spending scale on this idea.

## Boundaries and scale limits

No large language model, GPT-2-small-class training, packed GPU optimizer kernel, distributed training, or checkpointing study was run. Results are local proxy evidence for optimizer-state dynamics and accounting-level memory only.

## Claim scope

On an ill-conditioned quadratic and a small synthetic MLP classification task, 4-bit blockwise momentum with FP32 residual error compensation matched FP32 momentum convergence, but its residual storage made total momentum-state memory larger than plain FP32 momentum. The memory-saving no-error-compensation variant was weaker on the quadratic.

## Why it stopped

Medium proxy evidence was sufficient to falsify the combined claim for the tested FP32-residual EC design: convergence was preserved, but memory reduction was not.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded action is to test q8 or q4 compressed residual feedback and require total state below FP32 while matching FP32 convergence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compressed Residual Feedback for 4-Bit Momentum
- Success threshold: Compressed-residual 4-bit momentum uses less total state than FP32 and achieves quadratic final loss within 2x of FP32 plus classification validation loss within 0.01 absolute of FP32 across five seeds.
- Stop condition: Stop if compressed residual variants either exceed FP32 state bytes or miss the quadratic 2x final-loss threshold across five seeds.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-blockwise-momentum-with-error-compensation-e230a3e48c48`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
