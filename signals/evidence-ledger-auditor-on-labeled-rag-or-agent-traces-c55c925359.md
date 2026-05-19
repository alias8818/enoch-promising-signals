# Evidence ledger auditor on labeled RAG or agent traces

Status: `useful_signal`
Project ID: `evidence-ledger-auditor-on-labeled-rag-or-agent-traces-c55c925359`
Run ID: `evidence-ledger-auditor-on-labeled-rag-or-agent-traces-c55c925359-20260518T132105225950+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f96907f28b2e

## What looked useful

Invalid-detection F1 improved from 0.5714 for citation-presence baseline to 0.9610 for the evidence-ledger auditor at the primary threshold, with 0 false positives and 3 false negatives on 48 traces.

## Boundaries and scale limits

Small synthetic single-claim traces only; no real production RAG logs, no human annotation noise, no multi-claim answers, no adversarial paraphrase, and no independently validated semantic entailment model.

## Claim scope

On a deterministic Tier 1 set of 48 labeled synthetic RAG/agent-style traces with explicit evidence ledgers, a simple evidence-ledger auditor detected invalid claims substantially better than a citation-presence baseline.

## Why it stopped

Tier 1 controlled direct test supports the mechanism, but the evidence is synthetic and small, so this is useful no-paper evidence rather than publication readiness.

## Recommended next action

Run a medium confirmation on at least 200 independently labeled real or model-generated RAG/agent traces with multi-claim answers and a semantic entailment control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium real-trace confirmation for evidence-ledger auditing
- Success threshold: Invalid-detection F1 at least 0.15 higher than citation-presence baseline and valid-claim false-positive rate at or below 10%.
- Stop condition: Stop as negative if F1 gain is below 0.05, if valid-claim false-positive rate exceeds 20%, or if gains only appear on missing/unknown citation cases already solved by the baseline.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-auditor-on-labeled-rag-or-agent-traces-c55c925359`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
