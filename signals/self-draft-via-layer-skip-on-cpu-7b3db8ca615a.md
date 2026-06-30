# Self-Draft via Layer-Skip on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-draft-via-layer-skip-on-cpu-7b3db8ca615a`
Run ID: `self-draft-via-layer-skip-on-cpu-7b3db8ca615a-20260603T163913825063+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/247ced2927e2

## What looked useful

CPU self-drafting is highly sensitive to the match-rate/cost tradeoff: small skips were too expensive and large skips had low proxy agreement. The closest main-run case was 0.9939x at observed agreement 0.0425 versus break-even 0.0483.

## Boundaries and scale limits

No pretrained LLM, PyTorch, KV-cache implementation, or production inference kernel was tested. The result is a bounded proxy plus CPU timing model, not full trained-model validation.

## Claim scope

On this CPU-only worker, a NumPy residual language-model proxy did not show a layer-skip self-drafting speedup; observed skipped-layer top-1 agreement was below measured speculative break-even thresholds.

## Why it stopped

Stopped after a short proxy/early falsification: local CPU evidence did not show speedup and direct trained-model validation is still required to overturn the result.

## Recommended next action

Run a bounded direct GPT-2-small-class layer-skip speculative decoding test on a Python/PyTorch-compatible CPU host and require at least 1.10x end-to-end speedup before pursuing paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct GPT-2-small CPU layer-skip self-drafting test
- Success threshold: At least 1.10x median end-to-end speedup over full-depth greedy CPU decoding with identical output semantics or documented deterministic correction, and no less than 0.80 skipped/full top-1 agreement for the best configuration.
- Stop condition: Stop if no skip/draft-length configuration reaches 1.00x speedup or if top-1 agreement remains below the measured break-even threshold for all configurations.

## Evidence references

- Artifact root: `<local-path>/projects/self-draft-via-layer-skip-on-cpu-7b3db8ca615a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
