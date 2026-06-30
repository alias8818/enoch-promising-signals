# Per-Bit Residual Streams for INT4 GPT-2-small CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-bit-residual-streams-for-int4-gpt-2-small-cpu-87021e19dc7b`
Run ID: `per-bit-residual-streams-for-int4-gpt-2-small-cpu-87021e19dc7b-20260614T030449167117+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/59cbdc3df83e

## What looked useful

Naive bit-plane residual sidebands can optimize the wrong objective: the tested sideband cut weighted target-weight relative MSE by 5.8758% with 2.34375% sideband overhead, but worsened GPT-2-small NLL delta versus FP32 from +0.250825 to +0.261092 and worsened KL from 0.276925 to 0.296061 on the 64-sequence confirmation.

## Boundaries and scale limits

Directly tested GPT-2-small only, 48 non-embedding 2D projection weights, seq_len 128, 64 confirmation sequences from an embedded natural-prose corpus. No packed INT4 kernel, serving speedup, activation-aware fitting, full WikiText/OpenWebText benchmark, or larger model validation was performed.

## Claim scope

For GPT-2-small CPU post-training quality on a fixed local natural-text probe, a calibration-free per-bit residual sideband fitted only to INT4 projection-weight reconstruction error reduced target-weight MSE but did not improve NLL or KL versus plain per-output-channel INT4.

## Why it stopped

Direct bounded GPT-2-small evidence showed a proxy reconstruction win but target NLL/KL regression versus the simpler INT4 baseline, so the calibration-free per-bit weight-residual variant is not paper-worthy.

## Recommended next action

Stop this no-paper variant; if continuing locally, test an activation-aware or logit-aware bit-plane residual fit against plain INT4 on GPT-2-small before considering any packed-kernel or larger-model work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware per-bit residual fitting for INT4 GPT-2-small
- Success threshold: On at least 64 held-out seq_len-128 GPT-2-small sequences, activation-aware per-bit residual must reduce plain INT4 NLL delta by at least 0.02 and reduce KL by at least 5% with sideband overhead below 5% of INT4 payload.
- Stop condition: Stop if held-out NLL or KL is not better than plain INT4, or if sideband overhead exceeds 5% of INT4 payload before any packed-kernel work.

## Evidence references

- Artifact root: `<local-path>/projects/per-bit-residual-streams-for-int4-gpt-2-small-cpu-87021e19dc7b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
