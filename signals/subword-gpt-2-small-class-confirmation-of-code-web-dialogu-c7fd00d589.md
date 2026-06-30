# Subword GPT-2-small-class confirmation of code/web/dialogue mixture-ratio specialization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `subword-gpt-2-small-class-confirmation-of-code-web-dialogu-c7fd00d589`
Run ID: `subword-gpt-2-small-class-confirmation-of-code-web-dialogu-c7fd00d589-20260630T032723677778+0000`

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

- Parent run decision: Real-corpus tiny mixture confirmation for code/web/dialogue ratios: enoch://control-plane/projects/real-corpus-tiny-mixture-confirmation-for-code-web-dialogu-33584ec903/runs/real-corpus-tiny-mixture-confirmation-for-code-web-dialogu-33584ec903-20260630T025541848999+0000
- Parent run decision: Code/web/dialogue mixture ratios for tiny pretraining: enoch://control-plane/projects/code-web-dialogue-mixture-ratios-for-tiny-pretraining-e2a5a9936384/runs/code-web-dialogue-mixture-ratios-for-tiny-pretraining-e2a5a9936384-20260630T023924028677+0000

## What looked useful

Across three seeds, all 9 domain-heavy checks passed. Mean dominant-domain loss improvement versus balanced was 0.1831 nats/token for code, 0.0947 for web, and 0.0594 for dialogue. This supports the measurement harness and mechanism but not a publication-grade GPT-2-small claim.

## Boundaries and scale limits

Synthetic template corpora only; tiny 4-layer 256-hidden GPT-2-compatible model; 180 training steps per model; three seeds; no real public code/web/dialogue corpora; no GPT-2-small 124M run; no long-schedule or robustness validation.

## Claim scope

In a synthetic controlled probe using GPT-2 BPE tokenization and matched tiny GPT-2-compatible causal transformers, code-heavy, web-heavy, and dialogue-heavy mixture ratios reproducibly produced lower held-out loss on their dominant synthetic domain than the balanced control and made that domain the model's best held-out domain.

## Why it stopped

Closed as no-paper useful signal because the evidence is reproducible but synthetic/proxy-only, not a full validation of GPT-2-small-class specialization on real corpora.

## Recommended next action

Run the same mixture-ratio design on small real public code, web, and dialogue samples with a parameter-matched GPT-2-style model before considering any larger GPT-2-small-class validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus GPT-2 BPE mixture-ratio specialization probe
- Success threshold: At least 8 of 9 domain-heavy seed checks pass, where passing means the dominant domain is the model's best held-out domain and the dominant-domain loss improves over the balanced control by at least 0.02 nats/token.
- Stop condition: Stop as negative if fewer than 6 of 9 checks pass or if any real-domain result is dominated by data leakage, preprocessing artifacts, or inability to construct clean public splits.

## Evidence references

- Artifact root: `<local-path>/projects/subword-gpt-2-small-class-confirmation-of-code-web-dialogu-c7fd00d589`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
