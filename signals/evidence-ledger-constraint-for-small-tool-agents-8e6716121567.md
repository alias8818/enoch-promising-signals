# Evidence-ledger constraint for small tool agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-constraint-for-small-tool-agents-8e6716121567`
Run ID: `evidence-ledger-constraint-for-small-tool-agents-8e6716121567-20260527T150603435550+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0f7b5307e325

## What looked useful

A structured evidence ledger can act as a final-answer guardrail for small tool agents by preventing unsupported answer fields when the needed evidence is present. The boundary condition is upstream evidence quality: corrupted tool outputs are still propagated unless the ledger is paired with source validation or cross-checking.

## Boundaries and scale limits

Synthetic hidden knowledge base only; no real LLM, no natural-language retrieval, no public benchmark, no adversarial source trust model, and no large-scale serving or training validation. The result supports the ledger mechanism as a local proxy, not a broad paper-ready claim about deployed agents.

## Claim scope

In a deterministic synthetic tool-agent proxy with correct structured tools, answer-time evidence-ledger finalization reduced unsupported final claims from 18.34% of tasks to 0.00% over 25,000 tasks, with a small mean tool-call increase from 1.45052 to 1.50000. With 8% noisy tool documents, it reduced unsupported task rate from 20.18% to 2.816% but did not eliminate errors.

## Why it stopped

Proxy-only synthetic evidence supports the mechanism but is not direct or publication-grade validation for real language-model tool agents.

## Recommended next action

Stop this run as no-paper useful signal; next concrete action is a bounded real-small-LLM follow-up on a public tool-use QA benchmark using the same ledger finalization contract and matched tool budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-LLM evidence-ledger evaluation on public tool-use QA
- Success threshold: At least 500 real benchmark tasks; ledger condition lowers unsupported task rate by >=30% relative without >5% absolute accuracy loss and with <=20% additional tool calls.
- Stop condition: Stop if ledger extraction fails on >10% of tasks, if unsupported task rate reduction is <10%, or if accuracy drops by >10% absolute versus baseline.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-constraint-for-small-tool-agents-8e6716121567`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
