# Exact KV-Cache Context-Suffix Verification on Standard Text Prompts

Status: `useful_signal`
Project ID: `exact-kv-cache-context-suffix-verification-on-standard-tex-6b19508496`
Run ID: `exact-kv-cache-context-suffix-verification-on-standard-tex-6b19508496-20260519T054004629661+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a66c1f900995

## What looked useful

Identical suffix token IDs do not have prefix-independent KV-cache states in a standard causal Transformer: suffix-only KV/logits differed strongly from full-context suffix KV/logits, while one-shot full-prompt execution matched true incremental cached-prefix execution exactly in CPU/fp32.

## Boundaries and scale limits

Small controlled test only: one main GPT-2-class model, one tiny smoke model, 12 main examples, and a 4-example CPU/fp32 confirmation. No broad model-family survey and no approximate cache-reuse quality evaluation.

## Claim scope

Direct Tier 1 test of exact KV-cache suffix equivalence for identical token suffixes on WikiText-2 natural text prompts using distilgpt2 with 32-token prefixes and 32-token suffixes.

## Why it stopped

Direct small controlled test falsified exact KV-cache context-suffix equivalence on standard text prompts; this is not a full broad validation, but the CPU/fp32 counterexample is sufficient to reject the exact claim under the tested setup.

## Recommended next action

Stop this exact-equivalence line as a no-paper negative; any future work should reformulate around approximate reuse with explicit error tolerances and downstream task metrics.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/exact-kv-cache-context-suffix-verification-on-standard-tex-6b19508496`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
