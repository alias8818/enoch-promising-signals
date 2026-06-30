# GPT-2-small long-context priority KV residual quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gpt-2-small-long-context-priority-kv-residual-quantization-f96837100a`
Run ID: `gpt-2-small-long-context-priority-kv-residual-quantization-f96837100a-20260601T004232797020+0000`

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

- Parent run decision: Attention-Priority Asymmetric Residual Quantization: enoch://control-plane/projects/attention-priority-asymmetric-residual-quantization-323e85d544e9/runs/attention-priority-asymmetric-residual-quantization-323e85d544e9-20260531T153334964260+0000
- Parent run decision: Real Small-Transformer KV-Cache Attention-Priority Residual Quantization: enoch://control-plane/projects/real-small-transformer-kv-cache-attention-priority-residua-ac2c4618cb/runs/real-small-transformer-kv-cache-attention-priority-residua-ac2c4618cb-20260531T193313492680+0000

## What looked useful

Priority residual int4 KV quantization had mean delta NLL/token +0.00365 versus fp16, compared with +0.01253 for uniform int4 and +0.01052 for random same-budget residual. Paired priority-minus-uniform delta was -0.00887 NLL/token with approximate 95% CI [-0.01452, -0.00322]; priority-minus-random was -0.00687 with CI [-0.01175, -0.00199]. The advantage over recent-only and low-attention controls was directionally favorable but not closed. Priority int2 at the same residual budget was non-viable with +1.02690 NLL/token.

## Boundaries and scale limits

Inference-only GPT-2-small test inside the native 1024-token context window; no long-context retraining, no >1024-token validation, no fused compressed-cache runtime, and memory savings are algorithmic storage estimates rather than measured resident serving memory.

## Claim scope

On GPT-2-small cached decoding over 24 fixed-seed WikiText-2 validation windows with 768-token prefill and 64-token continuation, 4-bit per-token/per-head KV quantization with a 12.5% fp16 residual chosen by prefill attention priority reduced loss degradation versus uniform int4 and same-budget random residual controls while retaining an estimated 2.80x KV storage compression versus fp16.

## Why it stopped

Tier-2 local validation produced a useful but no-paper mechanism signal; it is not a full long-context or serving-runtime validation.

## Recommended next action

Run a bounded deepen follow-up at GPT-2's full 1024-token context with more windows and residual-fraction sweeps to close the priority-versus-recent and priority-versus-low-attention controls before considering any longer-context scale-out.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Full-window GPT-2 priority KV residual fraction sweep
- Success threshold: Priority int4 residual has mean delta NLL/token <= 0.01 versus fp16 and beats recent-only, low-attention, and random same-budget residual controls by >= 0.003 NLL/token with paired 95% confidence intervals below zero for at least one residual budget.
- Stop condition: Stop as no-paper negative if priority does not beat recent-only or low-attention controls at 1024-token context, or if all residual budgets exceed +0.01 mean NLL/token versus fp16.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-long-context-priority-kv-residual-quantization-f96837100a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
