# INT8 quantization for optimizer state reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-quantization-for-optimizer-state-reduction-5cb7a47c9d3b`
Run ID: `int8-quantization-for-optimizer-state-reduction-5cb7a47c9d3b-20260605T053311067723+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7718771a5fd1

## What looked useful

Naive INT8 compression of Adam second-moment state is the apparent failure point. First-moment-only INT8 compression is stable in this proxy but offers only partial memory reduction.

## Boundaries and scale limits

Synthetic binary classification task, small MLP, CPU NumPy implementation, 600 optimizer steps, 5 seeds; no LLMs, real datasets, CUDA kernels, distributed training, checkpoint restart tests, or long-horizon production framework validation.

## Claim scope

On a 5-seed synthetic NumPy MLP training proxy, persistent INT8 quantization of both Adam moments reduced optimizer-state bytes to about 25% of fp32 but caused unreliable convergence and a 14-16 percentage point mean validation-accuracy drop; INT8 first-moment-only storage preserved fp32-like convergence while reducing optimizer-state bytes to about 63% of fp32.

## Why it stopped

No-paper useful signal: the broad both-moment INT8 Adam-state hypothesis was falsified on a direct small proxy, while the stable first-moment-only result is too narrow and synthetic for a paper claim.

## Recommended next action

Run a bounded follow-up that replaces linear INT8 second-moment quantization with a nonnegative log-domain or float8-style representation and requires matched fp32 convergence without hidden fp32 residual state.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Log-domain 8-bit Adam second-moment state
- Success threshold: Both-moment 8-bit Adam-state variant uses no more than 35% of fp32 optimizer-state bytes and stays within 1 percentage point mean validation accuracy of fp32 over at least 5 seeds with zero collapsed seeds.
- Stop condition: Stop if any candidate second-moment representation either needs fp32 residual/shadow buffers that erase most memory savings or shows more than a 5 percentage point mean validation-accuracy drop on the synthetic proxy.

## Evidence references

- Artifact root: `<local-path>/projects/int8-quantization-for-optimizer-state-reduction-5cb7a47c9d3b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
