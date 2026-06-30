# Real-decoder validation of dynamic per-head KV residual windows

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-decoder-validation-of-dynamic-per-head-kv-residual-wi-49f2eece0a`
Run ID: `real-decoder-validation-of-dynamic-per-head-kv-residual-wi-49f2eece0a-20260522T023501162767+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Dynamic KV Cache 4-Bit with Per-Head Residual Window: enoch://control-plane/projects/dynamic-kv-cache-4-bit-with-per-head-residual-window-a8bd29a77fc9/runs/dynamic-kv-cache-4-bit-with-per-head-residual-window-a8bd29a77fc9-20260522T004704414853+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/71b83696c4f4

## What looked useful

Dynamic per-head windows with 4 sink tokens and thresholds 0.97/0.99 collapsed to about 11.5 retained tokens per head/layer and degraded NLL by +3.21 versus full cache, worse than fixed 16/32 controls. Fixed 64 + 4 sinks retained about 50.2 tokens per head/layer and stayed close to full cache with +0.064 NLL.

## Boundaries and scale limits

Small model, small embedded evaluation set, 128-token contexts, attention masking over full stored KV rather than a physical compacting/ragged KV cache; no production kernel or large-corpus validation.

## Claim scope

A Tier 1 direct test on distilgpt2 with 8 embedded natural-language passages and 128-token incremental decoding does not support a naive causal dynamic per-head residual-window policy based on previous-token attention mass.

## Why it stopped

Early direct falsification of the tested dynamic policy in a real pretrained decoder; not a full validation of all dynamic KV-window designs.

## Recommended next action

Stop this run as no-paper useful-signal evidence; a bounded follow-up should test a conservative dynamic policy with a minimum 64-token floor or explicit grow-back trigger against the fixed 64 + sink control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Conservative dynamic KV windows with grow-back against fixed 64 sink control
- Success threshold: Dynamic policy NLL no more than 0.05 above fixed 64 + 4 sinks and no more than 0.10 above full cache, while retaining at least 15% fewer mean KV tokens/head/layer than fixed 64 + 4 sinks.
- Stop condition: Stop if dynamic NLL is more than 0.10 worse than fixed 64 + 4 sinks or retained-token savings are below 10%, because that would not improve the demonstrated fixed-window control.

## Evidence references

- Artifact root: `<local-path>/projects/real-decoder-validation-of-dynamic-per-head-kv-residual-wi-49f2eece0a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
